# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "speech_synthesis: 0 messages, 1 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(speech_synthesis_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/chelsea/catkin_ws/src/speech_synthesis/srv/synthesis_service.srv" NAME_WE)
add_custom_target(_speech_synthesis_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "speech_synthesis" "/home/chelsea/catkin_ws/src/speech_synthesis/srv/synthesis_service.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(speech_synthesis
  "/home/chelsea/catkin_ws/src/speech_synthesis/srv/synthesis_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/speech_synthesis
)

### Generating Module File
_generate_module_cpp(speech_synthesis
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/speech_synthesis
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(speech_synthesis_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(speech_synthesis_generate_messages speech_synthesis_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chelsea/catkin_ws/src/speech_synthesis/srv/synthesis_service.srv" NAME_WE)
add_dependencies(speech_synthesis_generate_messages_cpp _speech_synthesis_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(speech_synthesis_gencpp)
add_dependencies(speech_synthesis_gencpp speech_synthesis_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS speech_synthesis_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(speech_synthesis
  "/home/chelsea/catkin_ws/src/speech_synthesis/srv/synthesis_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/speech_synthesis
)

### Generating Module File
_generate_module_eus(speech_synthesis
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/speech_synthesis
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(speech_synthesis_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(speech_synthesis_generate_messages speech_synthesis_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chelsea/catkin_ws/src/speech_synthesis/srv/synthesis_service.srv" NAME_WE)
add_dependencies(speech_synthesis_generate_messages_eus _speech_synthesis_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(speech_synthesis_geneus)
add_dependencies(speech_synthesis_geneus speech_synthesis_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS speech_synthesis_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(speech_synthesis
  "/home/chelsea/catkin_ws/src/speech_synthesis/srv/synthesis_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/speech_synthesis
)

### Generating Module File
_generate_module_lisp(speech_synthesis
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/speech_synthesis
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(speech_synthesis_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(speech_synthesis_generate_messages speech_synthesis_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chelsea/catkin_ws/src/speech_synthesis/srv/synthesis_service.srv" NAME_WE)
add_dependencies(speech_synthesis_generate_messages_lisp _speech_synthesis_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(speech_synthesis_genlisp)
add_dependencies(speech_synthesis_genlisp speech_synthesis_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS speech_synthesis_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(speech_synthesis
  "/home/chelsea/catkin_ws/src/speech_synthesis/srv/synthesis_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/speech_synthesis
)

### Generating Module File
_generate_module_nodejs(speech_synthesis
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/speech_synthesis
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(speech_synthesis_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(speech_synthesis_generate_messages speech_synthesis_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chelsea/catkin_ws/src/speech_synthesis/srv/synthesis_service.srv" NAME_WE)
add_dependencies(speech_synthesis_generate_messages_nodejs _speech_synthesis_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(speech_synthesis_gennodejs)
add_dependencies(speech_synthesis_gennodejs speech_synthesis_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS speech_synthesis_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(speech_synthesis
  "/home/chelsea/catkin_ws/src/speech_synthesis/srv/synthesis_service.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/speech_synthesis
)

### Generating Module File
_generate_module_py(speech_synthesis
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/speech_synthesis
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(speech_synthesis_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(speech_synthesis_generate_messages speech_synthesis_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/chelsea/catkin_ws/src/speech_synthesis/srv/synthesis_service.srv" NAME_WE)
add_dependencies(speech_synthesis_generate_messages_py _speech_synthesis_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(speech_synthesis_genpy)
add_dependencies(speech_synthesis_genpy speech_synthesis_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS speech_synthesis_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/speech_synthesis)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/speech_synthesis
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(speech_synthesis_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/speech_synthesis)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/speech_synthesis
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(speech_synthesis_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/speech_synthesis)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/speech_synthesis
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(speech_synthesis_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/speech_synthesis)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/speech_synthesis
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(speech_synthesis_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/speech_synthesis)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/speech_synthesis\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/speech_synthesis
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(speech_synthesis_generate_messages_py std_msgs_generate_messages_py)
endif()
