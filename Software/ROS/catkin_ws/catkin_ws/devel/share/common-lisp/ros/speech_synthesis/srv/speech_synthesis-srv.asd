
(cl:in-package :asdf)

(defsystem "speech_synthesis-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "synthesis_service" :depends-on ("_package_synthesis_service"))
    (:file "_package_synthesis_service" :depends-on ("_package"))
  ))