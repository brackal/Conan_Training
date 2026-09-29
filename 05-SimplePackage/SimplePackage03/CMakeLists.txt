cmake_minimum_required(VERSION 3.23.5)

project(segger-rtt LANGUAGES C CXX)

add_library(segger-rtt STATIC
    src/segger-rtt/SEGGER_RTT.c
    src/segger-rtt/SEGGER_RTT_printf.c
)

target_include_directories(segger-rtt
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/src/segger-rtt>
        $<INSTALL_INTERFACE:include>
)

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