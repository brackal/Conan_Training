# Using simple Conan:
you are here: 04-SimpleConanCross

#### For release with Unix Makefiles generator without Fmt. Fmt is not supported by Unix Makefiles
conan install . --build=missing --profile:host=RP2040_profile --profile:build=default
cmake -S . -B build  -G "Unix Makefiles" -DCMAKE_TOOLCHAIN_FILE="build/Release/generators/conan_toolchain.cmake"
cmake --build build

#### For release with Ninja generator, but still without Fmt
conan install . --build=missing --profile:host=RP2040_profile --profile:build=default
cmake -S . -B build  -G "Ninja" -DCMAKE_TOOLCHAIN_FILE="build/Release/generators/conan_toolchain.cmake"
ninja -C build

#### For release with Ninja generator and with Fmt. Ninja supports Fmt.
conan install . --build=missing --profile:host=RP2040_profile --profile:build=default -c tools.cmake.cmaketoolchain:generator=Ninja
cmake -S . -B build  -G "Ninja" -DCMAKE_TOOLCHAIN_FILE="build/Release/generators/conan_toolchain.cmake" -DCMAKE_BUILD_TYPE=Release
ninja -C build
