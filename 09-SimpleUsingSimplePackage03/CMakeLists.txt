
cmake_minimum_required(VERSION 3.23.5)

set(MY_PROJECT_NAME WellDoneApplication)
project(${MY_PROJECT_NAME} LANGUAGES C CXX)


add_executable(${MY_PROJECT_NAME} 
    src/main.cpp
    src/syscalls.c
)

target_include_directories(${MY_PROJECT_NAME}  PRIVATE src include)

find_package(segger-rtt REQUIRED)
if (segger-rtt_FOUND)
    message(STATUS "CMakeLists.txt: segger library is found!")
    target_link_libraries(${MY_PROJECT_NAME} PRIVATE segger-rtt::segger-rtt)
else()
    message(FATAL_ERROR "CMakeLists.txt: segger library not found!")
endif()

message(STATUS "CMakeLists.txt: Building with CMake version: ${CMAKE_VERSION}")
message(STATUS "CMakeLists.txt: Project ${MY_PROJECT_NAME} is cmaked!")