; Auto-generated. Do not edit!


(cl:in-package embedded_mas_examples-srv)


;//! \htmlinclude SumArray-request.msg.html

(cl:defclass <SumArray-request> (roslisp-msg-protocol:ros-message)
  ((v
    :reader v
    :initarg :v
    :type (cl:vector cl:integer)
   :initform (cl:make-array 0 :element-type 'cl:integer :initial-element 0)))
)

(cl:defclass SumArray-request (<SumArray-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SumArray-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SumArray-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name embedded_mas_examples-srv:<SumArray-request> is deprecated: use embedded_mas_examples-srv:SumArray-request instead.")))

(cl:ensure-generic-function 'v-val :lambda-list '(m))
(cl:defmethod v-val ((m <SumArray-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader embedded_mas_examples-srv:v-val is deprecated.  Use embedded_mas_examples-srv:v instead.")
  (v m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SumArray-request>) ostream)
  "Serializes a message object of type '<SumArray-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'v))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    ))
   (cl:slot-value msg 'v))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SumArray-request>) istream)
  "Deserializes a message object of type '<SumArray-request>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'v) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'v)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616)))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SumArray-request>)))
  "Returns string type for a service object of type '<SumArray-request>"
  "embedded_mas_examples/SumArrayRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SumArray-request)))
  "Returns string type for a service object of type 'SumArray-request"
  "embedded_mas_examples/SumArrayRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SumArray-request>)))
  "Returns md5sum for a message object of type '<SumArray-request>"
  "06b98b511eb27f6208b0367ed1441011")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SumArray-request)))
  "Returns md5sum for a message object of type 'SumArray-request"
  "06b98b511eb27f6208b0367ed1441011")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SumArray-request>)))
  "Returns full string definition for message of type '<SumArray-request>"
  (cl:format cl:nil "int64[] v~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SumArray-request)))
  "Returns full string definition for message of type 'SumArray-request"
  (cl:format cl:nil "int64[] v~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SumArray-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'v) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SumArray-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SumArray-request
    (cl:cons ':v (v msg))
))
;//! \htmlinclude SumArray-response.msg.html

(cl:defclass <SumArray-response> (roslisp-msg-protocol:ros-message)
  ((sum
    :reader sum
    :initarg :sum
    :type cl:integer
    :initform 0))
)

(cl:defclass SumArray-response (<SumArray-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SumArray-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SumArray-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name embedded_mas_examples-srv:<SumArray-response> is deprecated: use embedded_mas_examples-srv:SumArray-response instead.")))

(cl:ensure-generic-function 'sum-val :lambda-list '(m))
(cl:defmethod sum-val ((m <SumArray-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader embedded_mas_examples-srv:sum-val is deprecated.  Use embedded_mas_examples-srv:sum instead.")
  (sum m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SumArray-response>) ostream)
  "Serializes a message object of type '<SumArray-response>"
  (cl:let* ((signed (cl:slot-value msg 'sum)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SumArray-response>) istream)
  "Deserializes a message object of type '<SumArray-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'sum) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SumArray-response>)))
  "Returns string type for a service object of type '<SumArray-response>"
  "embedded_mas_examples/SumArrayResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SumArray-response)))
  "Returns string type for a service object of type 'SumArray-response"
  "embedded_mas_examples/SumArrayResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SumArray-response>)))
  "Returns md5sum for a message object of type '<SumArray-response>"
  "06b98b511eb27f6208b0367ed1441011")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SumArray-response)))
  "Returns md5sum for a message object of type 'SumArray-response"
  "06b98b511eb27f6208b0367ed1441011")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SumArray-response>)))
  "Returns full string definition for message of type '<SumArray-response>"
  (cl:format cl:nil "int64 sum~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SumArray-response)))
  "Returns full string definition for message of type 'SumArray-response"
  (cl:format cl:nil "int64 sum~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SumArray-response>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SumArray-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SumArray-response
    (cl:cons ':sum (sum msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SumArray)))
  'SumArray-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SumArray)))
  'SumArray-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SumArray)))
  "Returns string type for a service object of type '<SumArray>"
  "embedded_mas_examples/SumArray")