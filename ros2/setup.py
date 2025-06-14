from setuptools import find_packages, setup

package_name = 'embedded_mas_examples'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
           'time_listener = embedded_mas_examples.time_listener:main',
           'value_logger = embedded_mas_examples.value_logger:main',
           'value_writer = embedded_mas_examples.value_writer:main'
        ],
    },
)
