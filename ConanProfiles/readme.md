# Conan Profil

Ein Profil definiert die Zielumgebung: Betriebssystem, Architektur, Compiler, Build-Typ (Debug/Release) usw.

## Wo sind die Profile?
Die Conan Profile müssen sich befinden unter: 
~/.conan2/profiles/default
bzw.
C:\Users\UserName\.conan2\profiles

## Profil
[settings]
arch=x86_64
build_type=Release
compiler=msvc
compiler.cppstd=14
compiler.runtime=dynamic
compiler.version=193
os=Windows


#### Was jede Einstellung bedeutet
Setting             Bedeutung                       Beispielwerte
os                              Zielbetriebssystem          Windows, Linux, Macos
arch                            CPU-Architektur             x86_64, x86, armv8
build_type                  Debug oder Release       Debug, Release
compiler                    Compiler-Toolchain          msvc, gcc, clang
compiler.version        Version des Compilers       193 (MSVC 2022)
compiler.cppstd         C++-Sprachstandard          14, 17, 20, 23
compiler.runtime        Runtime-Linking             dynamic, static
compiler.runtime_type   Runtime-Variante        Debug, Release

Diese Kombination ergibt zusammen eine eindeutige Paket-ID (den sogenannten Package-Hash). Conan berechnet daraus einen Hash und sucht damit das passende vorkompilierte Binary.

os=Windows + arch=x86_64 + compiler=msvc + ... → bed280a9c51d41820ca64294cf373083ad852aa8
Ändert sich ein einziger Wert → anderer Hash → anderes Binary wird gesucht.


- compiler.cppstd=14 → Das gibt an, welchen C++-Sprachstandard Conan beim Bauen von Paketen verwenden soll, in diesem Fall C++14 (erschienen 2014).
- compiler.version → die MSVC/GCC/Clang-Toolchain-Version (z.B. 193 = MSVC 2022)
- compiler.runtime → ob die C++-Runtime statisch oder dynamisch gelinkt wird (static/dynamic)