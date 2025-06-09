#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <sensor_msgs/LaserScan.h>
#include <random>
#include <atomic>
#include <limits>

// Variável global atômica para uso seguro entre threads
std::atomic<float> min_distance_ahead(std::numeric_limits<float>::infinity());
std::atomic<bool> recebeu_scan(false);

// Callback para o tópico /scan
void scanCallback(const sensor_msgs::LaserScan::ConstPtr& scan_msg) {
    const auto& ranges = scan_msg->ranges;
    if (ranges.empty()) return;

    int index_center = ranges.size() / 2;
    if (index_center < ranges.size()) {
        float distance = ranges[index_center];
        if (!std::isnan(distance) && !std::isinf(distance)) {
            min_distance_ahead.store(distance, std::memory_order_relaxed);
            recebeu_scan.store(true, std::memory_order_relaxed);
        } else {
            min_distance_ahead.store(std::numeric_limits<float>::infinity(), std::memory_order_relaxed);
        }
    }
}

int main(int argc, char** argv) {
    ros::init(argc, argv, "random_cmd_vel_publisher");
    ros::NodeHandle nh;

    ros::Publisher cmd_vel_pub = nh.advertise<geometry_msgs::Twist>("/cmd_vel", 10);
    ros::Subscriber scan_sub = nh.subscribe("/scan", 1, scanCallback);

    // Usa spinner assíncrono para melhor desempenho
    ros::AsyncSpinner spinner(2);
    spinner.start();

    ROS_INFO("Aguardando leitura válida do LiDAR (/scan)...");
    ros::Rate wait_rate(10);
    while (ros::ok() && !recebeu_scan.load(std::memory_order_relaxed)) {
        wait_rate.sleep();
    }
    ROS_INFO("Leitura válida recebida. Iniciando controle de movimento xy.");

    // Inicializa geradores de números aleatórios
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<float> linear_dist(-0.5f, 0.5f);
    std::uniform_real_distribution<float> angular_dist(-1.0f, 1.0f);

    ros::Rate rate(10);  // 10 Hz
    geometry_msgs::Twist msg;

    int iteration = 0;
    const int max_iterations = 10000;

    while (ros::ok() && iteration < max_iterations) {
        float current_distance = min_distance_ahead.load(std::memory_order_relaxed);

        if (current_distance < 0.2f) {
            msg.linear.x = -0.2f;
            msg.angular.z = 0.0f;
        } else {
            msg.linear.x = linear_dist(gen);
            msg.angular.z = angular_dist(gen);
        }

        cmd_vel_pub.publish(msg);
        rate.sleep();
        ++iteration;
    }

    ROS_INFO("Encerrando após %d iterações.", max_iterations);

    spinner.stop();
    return 0;
}

