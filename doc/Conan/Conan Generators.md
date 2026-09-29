## Was macht `generators = "CMakeToolchain", "CMakeDeps"`?

Sie sagt Conan: "Wenn du `conan install` ausführst, erzeuge am Ende automatisch diese beiden Sets von Dateien, damit CMake meine Abhängigkeiten und Compiler-Einstellungen versteht."

Es sind zwei unterschiedliche Generatoren mit unterschiedlichen Aufgaben:

### `CMakeToolchain`

Erzeugt eine Datei namens `conan_toolchain.cmake`. Diese enthält **projektweite Build-Einstellungen**, z. B.:

- Compiler-Flags (z. B. für C++-Standard)
- Build-Type (Debug/Release)
- Architektur-Einstellungen
- Plattformspezifische CMake-Variablen

Du bindest sie beim Konfigurieren ein:

```bash
cmake -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake ..
```

Das ersetzt praktisch manuelles Setzen von CMake-Variablen für Compiler/Architektur.

### `CMakeDeps`

Erzeugt für **jede einzelne Abhängigkeit** eine passende CMake-Config-Datei, z. B. bei `fmt/10.2.1`:

- `fmt-config.cmake`
- `fmtTargets.cmake`
- `fmtTarget-release.cmake`

Diese Dateien machen es möglich, dass du in deinem `CMakeLists.txt` ganz normal schreibst:

```cmake
find_package(fmt REQUIRED)
target_link_libraries(mein_programm fmt::fmt)
```

CMake findet die Bibliothek dann automatisch – mit korrekten Include-Pfaden, Lib-Pfaden usw. — ohne dass du das per Hand suchen musst.

## Was sind "Generator-Dateien" allgemein?

Generator-Dateien sind die **Brücke zwischen Conan und deinem Build-System**. Conan selbst baut nicht dein Projekt – es verwaltet nur Pakete/Abhängigkeiten. Damit dein eigentliches Build-Tool (CMake, Meson, MSBuild, Bazel, Makefiles, Visual Studio, ...) weiß:

- wo die Header-Dateien der Abhängigkeiten liegen
- wo die kompilierten Bibliotheken (`.lib`, `.a`, `.so`, `.dll`) liegen
- welche Compiler-Flags/Definitionen nötig sind
- welche Version/Konfiguration (Debug/Release) verwendet werden soll

… generiert Conan automatisch Dateien in der jeweiligen "Sprache" des Build-Systems. Es gibt viele solcher Generatoren, je nach Ziel-Toolchain:

|Generator|Für welches Tool|
|---|---|
|`CMakeToolchain` + `CMakeDeps`|CMake (modern)|
|`MesonToolchain` + `PkgConfigDeps`|Meson|
|`MSBuildToolchain` + `MSBuildDeps`|Visual Studio/MSBuild|
|`MakeDeps`|Makefiles|
|`PkgConfigDeps`|pkg-config (allgemein, z. B. für Autotools)|

**Kurz gesagt:** `generators = "CMakeToolchain", "CMakeDeps"` weist Conan an, beim `conan install` automatisch die CMake-kompatiblen Dateien zu erzeugen, damit `find_package()` in deinem `CMakeLists.txt` funktioniert und dein Projekt ohne manuelles Pfad-Gefrickel kompiliert werden kann.


[[Conan Profile]]