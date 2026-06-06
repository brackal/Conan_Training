
cmake_minimum_required(VERSION 3.23.5)

set(MY_PROJECT_NAME WellDoneApplication)
set(ARM_ARCH "cortex-m0plus")

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


# ─── Compile + Link Flags zusammen definieren ────────────────────────────────
set(ARM_FLAGS
    -mcpu=${ARM_ARCH}       # Erzeuge Code optimiert für genau diesen CPU-Kern
    -mthumb                 # Thumb-Mode (16-bit Instruktionen) für Cortex-M
    -mfloat-abi=soft        # Kein FPU auf Cortex-M0+ -> Fliesskommazahlen sind in Software emuliert
    -Os                     # Optimierung für Größe (empfohlen für Embedded)
)

target_compile_options(${MY_PROJECT_NAME} PRIVATE
    ${ARM_FLAGS}
    -ffunction-sections    # Jede Funktion in eigene Section → gc-sections greift besser
    -fdata-sections        # Gleiches für Daten
    -fno-exceptions        # Empfohlen für Bare-Metal (spart Flash)
    -fno-rtti              # Kein RTTI (spart Flash)
)

target_link_options(${MY_PROJECT_NAME} PRIVATE
    ${ARM_FLAGS}
    -specs=nosys.specs
    -specs=nano.specs
    "LINKER:--gc-sections"
    "LINKER:-Map=${MY_PROJECT_NAME}.map"
    # -T${CMAKE_SOURCE_DIR}/linker/rp2040.ld   # Linker-Script wenn noetig
)

add_custom_command(TARGET ${MY_PROJECT_NAME} POST_BUILD
    COMMAND ${CMAKE_OBJCOPY} -O binary 
        ${MY_PROJECT_NAME} ${MY_PROJECT_NAME}.bin
)

message(STATUS "CMakeLists.txt: Building with CMake version: ${CMAKE_VERSION}")
message(STATUS "CMakeLists.txt: Project ${MY_PROJECT_NAME} is cmaked!")
