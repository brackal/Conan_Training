# Using simple CMake:
you are here: 01-SimpleCMake

mkdir build
cd build
cmake -G "Visual Studio 17 2022" ..
cmake --build .

Kurz erklärt:

**Zeile 3: `cmake -G "Visual Studio 17 2022" ..`**

- `cmake` – ruft CMake auf, das Build-System-Konfigurationstool
- `-G "Visual Studio 17 2022"` – Option `-G` legt den **Generator** fest, also welches Build-System erzeugt wird. Hier: Projektdateien für Visual Studio 2022 (Version 17)
- `..` – Pfad zum Verzeichnis mit der `CMakeLists.txt` (das übergeordnete Verzeichnis). Das bedeutet: Der Befehl wird aus einem separaten Build-Ordner heraus ausgeführt (Out-of-Source-Build), und CMake liest die Quell-/Projektdefinition aus dem Elternverzeichnis

→ Ergebnis: Erzeugt eine `.sln`-Datei (Visual-Studio-Solution) und zugehörige Projektdateien im aktuellen Verzeichnis.

**Zeile 4: `cmake --build .`**

- `cmake --build` – plattformunabhängiger Befehl zum **Kompilieren**, ruft im Hintergrund den passenden Builder auf (hier: MSBuild von Visual Studio)
- `.` – gibt an, dass sich die zu bauenden Projektdateien im aktuellen Verzeichnis befinden

→ Ergebnis: Baut das Projekt (Standard-Konfiguration, meist Debug), ohne dass man Visual Studio manuell öffnen muss.

[[Generators]] [[CMake]] [[Build-System]]