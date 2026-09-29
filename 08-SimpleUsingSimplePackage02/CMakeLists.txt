
cmake_minimum_required(VERSION 3.23.5)

set(MY_PROJECT_NAME WellDoneApplication)
project(${MY_PROJECT_NAME} LANGUAGES CXX)


add_executable(${MY_PROJECT_NAME} 
    src/main.cpp
    src/Guitar.cpp
    src/Inventory.cpp

    libs/hello/hello.cpp
)

target_include_directories(${MY_PROJECT_NAME}  PRIVATE src libs)

#find_package(hello-library REQUIRED)
#target_link_libraries(${MY_PROJECT_NAME} PRIVATE hello-library::hello-library)
# .cpp Dateien direkt in Consumer compilieren:
#target_sources(${MY_PROJECT_NAME} PRIVATE ${hello-library_SOURCE_DIR}/hello.cpp)


message(STATUS "CMakeLists.txt: Building with CMake version: ${CMAKE_VERSION}")
message(STATUS "CMakeLists.txt: Project ${MY_PROJECT_NAME} is cmaked!")