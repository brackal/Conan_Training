# Using simple Conan:
you are here: 10-SimpleUsingSimplePackage05

in diesem projekt wird ein segger-rtt Conan Paket includiert, das nur aus sourcen .h und .c besteht. Sourcen werden von consumer Projekt gebaut, dabei wirden die sourcen nicht in das Projektverzeichnis gespeichert, sondern im cache des conans gebaut.

conan install . --build=missing --profile:host=RP2040_profile --profile:build=default
cmake --preset conan-release
cmake --build build/Release


#das geht nicht
cmake -S . -B build/Release -DCMAKE_BUILD_TYPE=Release  -G "Unix Makefiles" -DCMAKE_TOOLCHAIN_FILE="build/Release/generators/conan_toolchain.cmake"


