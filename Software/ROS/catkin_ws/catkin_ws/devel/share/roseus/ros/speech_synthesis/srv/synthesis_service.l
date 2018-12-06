;; Auto-generated. Do not edit!


(when (boundp 'speech_synthesis::synthesis_service)
  (if (not (find-package "SPEECH_SYNTHESIS"))
    (make-package "SPEECH_SYNTHESIS"))
  (shadow 'synthesis_service (find-package "SPEECH_SYNTHESIS")))
(unless (find-package "SPEECH_SYNTHESIS::SYNTHESIS_SERVICE")
  (make-package "SPEECH_SYNTHESIS::SYNTHESIS_SERVICE"))
(unless (find-package "SPEECH_SYNTHESIS::SYNTHESIS_SERVICEREQUEST")
  (make-package "SPEECH_SYNTHESIS::SYNTHESIS_SERVICEREQUEST"))
(unless (find-package "SPEECH_SYNTHESIS::SYNTHESIS_SERVICERESPONSE")
  (make-package "SPEECH_SYNTHESIS::SYNTHESIS_SERVICERESPONSE"))

(in-package "ROS")





(defclass speech_synthesis::synthesis_serviceRequest
  :super ros::object
  :slots (_req ))

(defmethod speech_synthesis::synthesis_serviceRequest
  (:init
   (&key
    ((:req __req) "")
    )
   (send-super :init)
   (setq _req (string __req))
   self)
  (:req
   (&optional __req)
   (if __req (setq _req __req)) _req)
  (:serialization-length
   ()
   (+
    ;; string _req
    4 (length _req)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _req
       (write-long (length _req) s) (princ _req s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _req
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _req (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass speech_synthesis::synthesis_serviceResponse
  :super ros::object
  :slots (_res ))

(defmethod speech_synthesis::synthesis_serviceResponse
  (:init
   (&key
    ((:res __res) 0)
    )
   (send-super :init)
   (setq _res (round __res))
   self)
  (:res
   (&optional __res)
   (if __res (setq _res __res)) _res)
  (:serialization-length
   ()
   (+
    ;; int32 _res
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _res
       (write-long _res s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _res
     (setq _res (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass speech_synthesis::synthesis_service
  :super ros::object
  :slots ())

(setf (get speech_synthesis::synthesis_service :md5sum-) "d5bb794ce9c6117c55c80145b1c203b2")
(setf (get speech_synthesis::synthesis_service :datatype-) "speech_synthesis/synthesis_service")
(setf (get speech_synthesis::synthesis_service :request) speech_synthesis::synthesis_serviceRequest)
(setf (get speech_synthesis::synthesis_service :response) speech_synthesis::synthesis_serviceResponse)

(defmethod speech_synthesis::synthesis_serviceRequest
  (:response () (instance speech_synthesis::synthesis_serviceResponse :init)))

(setf (get speech_synthesis::synthesis_serviceRequest :md5sum-) "d5bb794ce9c6117c55c80145b1c203b2")
(setf (get speech_synthesis::synthesis_serviceRequest :datatype-) "speech_synthesis/synthesis_serviceRequest")
(setf (get speech_synthesis::synthesis_serviceRequest :definition-)
      "string req
---
int32 res

")

(setf (get speech_synthesis::synthesis_serviceResponse :md5sum-) "d5bb794ce9c6117c55c80145b1c203b2")
(setf (get speech_synthesis::synthesis_serviceResponse :datatype-) "speech_synthesis/synthesis_serviceResponse")
(setf (get speech_synthesis::synthesis_serviceResponse :definition-)
      "string req
---
int32 res

")



(provide :speech_synthesis/synthesis_service "d5bb794ce9c6117c55c80145b1c203b2")


