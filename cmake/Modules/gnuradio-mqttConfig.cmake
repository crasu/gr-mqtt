INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_MQTT mqtt)

FIND_PATH(
    MQTT_INCLUDE_DIRS
    NAMES mqtt/api.h
    HINTS $ENV{MQTT_DIR}/include
        ${PC_MQTT_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    MQTT_LIBRARIES
    NAMES gnuradio-mqtt
    HINTS $ENV{MQTT_DIR}/lib
        ${PC_MQTT_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(MQTT DEFAULT_MSG MQTT_LIBRARIES MQTT_INCLUDE_DIRS)
MARK_AS_ADVANCED(MQTT_LIBRARIES MQTT_INCLUDE_DIRS)

