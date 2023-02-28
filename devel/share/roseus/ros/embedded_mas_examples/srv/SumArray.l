;; Auto-generated. Do not edit!


(when (boundp 'embedded_mas_examples::SumArray)
  (if (not (find-package "EMBEDDED_MAS_EXAMPLES"))
    (make-package "EMBEDDED_MAS_EXAMPLES"))
  (shadow 'SumArray (find-package "EMBEDDED_MAS_EXAMPLES")))
(unless (find-package "EMBEDDED_MAS_EXAMPLES::SUMARRAY")
  (make-package "EMBEDDED_MAS_EXAMPLES::SUMARRAY"))
(unless (find-package "EMBEDDED_MAS_EXAMPLES::SUMARRAYREQUEST")
  (make-package "EMBEDDED_MAS_EXAMPLES::SUMARRAYREQUEST"))
(unless (find-package "EMBEDDED_MAS_EXAMPLES::SUMARRAYRESPONSE")
  (make-package "EMBEDDED_MAS_EXAMPLES::SUMARRAYRESPONSE"))

(in-package "ROS")





(defclass embedded_mas_examples::SumArrayRequest
  :super ros::object
  :slots (_v ))

(defmethod embedded_mas_examples::SumArrayRequest
  (:init
   (&key
    ((:v __v) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _v __v)
   self)
  (:v
   (&optional __v)
   (if __v (setq _v __v)) _v)
  (:serialization-length
   ()
   (+
    ;; int64[] _v
    (* 8    (length _v)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64[] _v
     (write-long (length _v) s)
     (dotimes (i (length _v))
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke (elt _v i) (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class (elt _v i)) (= (length ((elt _v i) . bv)) 2)) ;; bignum
              (write-long (ash (elt ((elt _v i) . bv) 0) 0) s)
              (write-long (ash (elt ((elt _v i) . bv) 1) -1) s))
             ((and (class (elt _v i)) (= (length ((elt _v i) . bv)) 1)) ;; big1
              (write-long (elt ((elt _v i) . bv) 0) s)
              (write-long (if (>= (elt _v i) 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long (elt _v i) s)(write-long (if (>= (elt _v i) 0) 0 #xffffffff) s)))
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64[] _v
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _v (instantiate integer-vector n))
     (dotimes (i n)
#+(or :alpha :irix6 :x86_64)
      (setf (elt _v i) (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf (elt _v i) (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
     ))
   ;;
   self)
  )

(defclass embedded_mas_examples::SumArrayResponse
  :super ros::object
  :slots (_sum ))

(defmethod embedded_mas_examples::SumArrayResponse
  (:init
   (&key
    ((:sum __sum) 0)
    )
   (send-super :init)
   (setq _sum (round __sum))
   self)
  (:sum
   (&optional __sum)
   (if __sum (setq _sum __sum)) _sum)
  (:serialization-length
   ()
   (+
    ;; int64 _sum
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _sum
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _sum (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _sum) (= (length (_sum . bv)) 2)) ;; bignum
              (write-long (ash (elt (_sum . bv) 0) 0) s)
              (write-long (ash (elt (_sum . bv) 1) -1) s))
             ((and (class _sum) (= (length (_sum . bv)) 1)) ;; big1
              (write-long (elt (_sum . bv) 0) s)
              (write-long (if (>= _sum 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _sum s)(write-long (if (>= _sum 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _sum
#+(or :alpha :irix6 :x86_64)
      (setf _sum (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _sum (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass embedded_mas_examples::SumArray
  :super ros::object
  :slots ())

(setf (get embedded_mas_examples::SumArray :md5sum-) "06b98b511eb27f6208b0367ed1441011")
(setf (get embedded_mas_examples::SumArray :datatype-) "embedded_mas_examples/SumArray")
(setf (get embedded_mas_examples::SumArray :request) embedded_mas_examples::SumArrayRequest)
(setf (get embedded_mas_examples::SumArray :response) embedded_mas_examples::SumArrayResponse)

(defmethod embedded_mas_examples::SumArrayRequest
  (:response () (instance embedded_mas_examples::SumArrayResponse :init)))

(setf (get embedded_mas_examples::SumArrayRequest :md5sum-) "06b98b511eb27f6208b0367ed1441011")
(setf (get embedded_mas_examples::SumArrayRequest :datatype-) "embedded_mas_examples/SumArrayRequest")
(setf (get embedded_mas_examples::SumArrayRequest :definition-)
      "int64[] v
---
int64 sum

")

(setf (get embedded_mas_examples::SumArrayResponse :md5sum-) "06b98b511eb27f6208b0367ed1441011")
(setf (get embedded_mas_examples::SumArrayResponse :datatype-) "embedded_mas_examples/SumArrayResponse")
(setf (get embedded_mas_examples::SumArrayResponse :definition-)
      "int64[] v
---
int64 sum

")



(provide :embedded_mas_examples/SumArray "06b98b511eb27f6208b0367ed1441011")


