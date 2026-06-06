
cmake_minimum_required(VERSION 3.23.5)

set(MY_PROJECT_NAME WellDoneApplication)
project(${MY_PROJECT_NAME} LANGUAGES CXX)


add_executable(${MY_PROJECT_NAME} 
    src/main.cpp
    src/Guitar.cpp
    src/Inventory.cpp
)

target_include_directories(${MY_PROJECT_NAME}  PRIVATE src)


message(STATUS "CMakeLists.txt: Building with CMake version: ${CMAKE_VERSION}")
message(STATUS "CMakeLists.txt: Project ${MY_PROJECT_NAME} is cmaked!")