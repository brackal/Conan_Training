Eine "Build-Datei" ist die vom Generator (z. B. CMake) erzeugte Datei, die das eigentliche Build-Tool ausführt. Beispiele:

|Generator|Build-Datei|
|---|---|
|Unix Makefiles|`Makefile`|
|Ninja|`build.ninja`|
|Visual Studio|`.sln` / `.vcxproj`|

Sie enthält den Abhängigkeitsgraphen und die konkreten Compiler-/Linker-Befehle. Das Build-Tool (`make`, `ninja`, `MSBuild`) liest diese Datei und führt sie aus.
