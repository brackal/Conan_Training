# Using simple Conan:
you are here: 09-SimpleUsingSimplePackage03


conan install . --build=missing --profile:host=RP2040_profile --profile:build=default

cmake -S . -B build/Release -DCMAKE_BUILD_TYPE=Release  -G "Unix Makefiles" -DCMAKE_TOOLCHAIN_FILE="build/Release/generators/conan_toolchain.cmake"

cmake --build build/Release
