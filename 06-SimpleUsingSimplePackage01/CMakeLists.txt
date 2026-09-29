
cmake_minimum_required(VERSION 3.23.5)

set(MY_PROJECT_NAME WellDoneApplication)
project(${MY_PROJECT_NAME} LANGUAGES CXX)


add_executable(${MY_PROJECT_NAME} 
    src/main.cpp
    src/Guitar.cpp
    src/Inventory.cpp
)

target_include_directories(${MY_PROJECT_NAME}  PRIVATE src)



# Von Conan generierte Pakete finden
find_package(fmt REQUIRED)
if (fmt_FOUND)
    message(STATUS "CMakeLists.txt: fmt library is found!")
    target_link_libraries(${MY_PROJECT_NAME} PRIVATE fmt::fmt)
else()
    message(FATAL_ERROR "CMakeLists.txt: fmt library not found!")
endif()

find_package(hello REQUIRED)
if (hello_FOUND)
    message(STATUS "CMakeLists.txt: hello library is found!")
    target_link_libraries(${MY_PROJECT_NAME} PRIVATE hello::hello)
else()
    message(FATAL_ERROR "CMakeLists.txt: hello library not found!")
endif()

message(STATUS "CMakeLists.txt: Building with CMake version: ${CMAKE_VERSION}")
message(STATUS "CMakeLists.txt: Project ${MY_PROJECT_NAME} is cmaked!")