
cmake_minimum_required(VERSION 3.23.5)

set(MY_PROJECT_NAME WellDoneApplication)
project(${MY_PROJECT_NAME} LANGUAGES C CXX)


find_package(segger-rtt REQUIRED)
message(STATUS "SEGGER_SRC_DIR = ${SEGGER_SRC_DIR}")
file(GLOB SEGGER_SOURCES "${SEGGER_SRC_DIR}/*.c")
message(STATUS "SEGGER_SOURCES = ${SEGGER_SOURCES}")   # zur Diagnose!




add_executable(${MY_PROJECT_NAME} 
    src/main.cpp
    src/syscalls.c
    ${SEGGER_SOURCES}
)

target_include_directories(${MY_PROJECT_NAME}  PRIVATE src include ${segger_INCLUDE_DIRS})

target_link_libraries(${MY_PROJECT_NAME} PRIVATE segger-rtt::segger-rtt)
