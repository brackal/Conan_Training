# Using simple Conan:
you are here: 07-SimpleUsingSimplePackage02


### Case: Package consists of source files
##### In this case conan copies the files from the required package into the application directory. Both: the required package and the target application directory are defined in the conanfile. Application cmake builds (compiles) all sources (src/ and libs/) itself after the conan install. Note: as build_type and --config you can select Release or Debug

conan install . --build=missing --output-folder=build -s build_type=Release
cd build/
cmake -G "Visual Studio 17 2022" ..
cmake --build . --config Release
