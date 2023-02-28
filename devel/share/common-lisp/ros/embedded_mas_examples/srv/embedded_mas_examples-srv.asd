
(cl:in-package :asdf)

(defsystem "embedded_mas_examples-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "SumArray" :depends-on ("_package_SumArray"))
    (:file "_package_SumArray" :depends-on ("_package"))
  ))