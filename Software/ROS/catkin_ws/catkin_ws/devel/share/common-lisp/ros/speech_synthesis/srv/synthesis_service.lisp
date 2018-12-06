; Auto-generated. Do not edit!


(cl:in-package speech_synthesis-srv)


;//! \htmlinclude synthesis_service-request.msg.html

(cl:defclass <synthesis_service-request> (roslisp-msg-protocol:ros-message)
  ((req
    :reader req
    :initarg :req
    :type cl:string
    :initform ""))
)

(cl:defclass synthesis_service-request (<synthesis_service-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <synthesis_service-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'synthesis_service-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name speech_synthesis-srv:<synthesis_service-request> is deprecated: use speech_synthesis-srv:synthesis_service-request instead.")))

(cl:ensure-generic-function 'req-val :lambda-list '(m))
(cl:defmethod req-val ((m <synthesis_service-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader speech_synthesis-srv:req-val is deprecated.  Use speech_synthesis-srv:req instead.")
  (req m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <synthesis_service-request>) ostream)
  "Serializes a message object of type '<synthesis_service-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'req))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'req))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <synthesis_service-request>) istream)
  "Deserializes a message object of type '<synthesis_service-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'req) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'req) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<synthesis_service-request>)))
  "Returns string type for a service object of type '<synthesis_service-request>"
  "speech_synthesis/synthesis_serviceRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'synthesis_service-request)))
  "Returns string type for a service object of type 'synthesis_service-request"
  "speech_synthesis/synthesis_serviceRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<synthesis_service-request>)))
  "Returns md5sum for a message object of type '<synthesis_service-request>"
  "d5bb794ce9c6117c55c80145b1c203b2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'synthesis_service-request)))
  "Returns md5sum for a message object of type 'synthesis_service-request"
  "d5bb794ce9c6117c55c80145b1c203b2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<synthesis_service-request>)))
  "Returns full string definition for message of type '<synthesis_service-request>"
  (cl:format cl:nil "string req~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'synthesis_service-request)))
  "Returns full string definition for message of type 'synthesis_service-request"
  (cl:format cl:nil "string req~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <synthesis_service-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'req))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <synthesis_service-request>))
  "Converts a ROS message object to a list"
  (cl:list 'synthesis_service-request
    (cl:cons ':req (req msg))
))
;//! \htmlinclude synthesis_service-response.msg.html

(cl:defclass <synthesis_service-response> (roslisp-msg-protocol:ros-message)
  ((res
    :reader res
    :initarg :res
    :type cl:integer
    :initform 0))
)

(cl:defclass synthesis_service-response (<synthesis_service-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <synthesis_service-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'synthesis_service-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name speech_synthesis-srv:<synthesis_service-response> is deprecated: use speech_synthesis-srv:synthesis_service-response instead.")))

(cl:ensure-generic-function 'res-val :lambda-list '(m))
(cl:defmethod res-val ((m <synthesis_service-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader speech_synthesis-srv:res-val is deprecated.  Use speech_synthesis-srv:res instead.")
  (res m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <synthesis_service-response>) ostream)
  "Serializes a message object of type '<synthesis_service-response>"
  (cl:let* ((signed (cl:slot-value msg 'res)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <synthesis_service-response>) istream)
  "Deserializes a message object of type '<synthesis_service-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'res) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<synthesis_service-response>)))
  "Returns string type for a service object of type '<synthesis_service-response>"
  "speech_synthesis/synthesis_serviceResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'synthesis_service-response)))
  "Returns string type for a service object of type 'synthesis_service-response"
  "speech_synthesis/synthesis_serviceResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<synthesis_service-response>)))
  "Returns md5sum for a message object of type '<synthesis_service-response>"
  "d5bb794ce9c6117c55c80145b1c203b2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'synthesis_service-response)))
  "Returns md5sum for a message object of type 'synthesis_service-response"
  "d5bb794ce9c6117c55c80145b1c203b2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<synthesis_service-response>)))
  "Returns full string definition for message of type '<synthesis_service-response>"
  (cl:format cl:nil "int32 res~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'synthesis_service-response)))
  "Returns full string definition for message of type 'synthesis_service-response"
  (cl:format cl:nil "int32 res~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <synthesis_service-response>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <synthesis_service-response>))
  "Converts a ROS message object to a list"
  (cl:list 'synthesis_service-response
    (cl:cons ':res (res msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'synthesis_service)))
  'synthesis_service-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'synthesis_service)))
  'synthesis_service-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'synthesis_service)))
  "Returns string type for a service object of type '<synthesis_service>"
  "speech_synthesis/synthesis_service")