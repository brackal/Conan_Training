cmake_minimum_required(VERSION 3.23.5)

project(segger-rtt LANGUAGES C CXX)


message(STATUS "CMAKE_CURRENT_SOURCE_DIR = ${CMAKE_CURRENT_SOURCE_DIR}")
message(STATUS "Gefundene SOURCES = ${SOURCES}")

file(GLOB_RECURSE SOURCES "${SEGGER_SOURCE_DIR}/RTT/*.c") 

add_library(segger-rtt STATIC ${SOURCES})
target_include_directories(segger-rtt PUBLIC 
    ${SEGGER_SOURCE_DIR}/RTT
    ${SEGGER_SOURCE_DIR}/Config)




# Architektur-/Optimierungs-Flags fürs Kompilieren der Lib selbst.
# -mcpu/-mthumb sollten idealerweise zentral aus dem Toolchain-File kommen,
# hier nur falls das Profil das nicht bereits global setzt.
target_compile_options(segger-rtt PRIVATE
    -Os
    -ffunction-sections
    -fdata-sections
)

install(TARGETS segger-rtt
    ARCHIVE DESTINATION lib
)
install(DIRECTORY src/segger-rtt/
    DESTINATION include
    FILES_MATCHING PATTERN "*.h"
)