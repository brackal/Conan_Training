# Using simple Conan:
you are here: 03-SimpleConanPy

#### For debug
conan install . --build=missing --profile=default_debug
#### Or for release
conan profile detect --force
conan install . --build=missing --profile=default

cd build
#### Assuming Visual Studio 17 2022 is your VS version and that it matches your default profile
cmake .. -G "Visual Studio 17 2022" -DCMAKE_TOOLCHAIN_FILE="generators/conan_toolchain.cmake"
cmake --build .


#### If you want cmake without cd build -> do this:
conan install . --build=missing --profile=default_debug
cmake -S . -B build -G "Visual Studio 17 2022" -DCMAKE_TOOLCHAIN_FILE="generators/conan_toolchain.cmake"
cmake --build build


#### If you want build only by using conan (for that reason you need to define in conanfile.py build_requirements(self) and build(self)):
you are here: 03-SimpleConanPy
#### For debug
conan install . --build=missing --profile=default_debug
conan build . --profile=default_debug
#### Or for release
conan install . --build=missing --profile=default
conan build . --profile=default