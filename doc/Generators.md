Kurze Übersicht gängiger CMake-Generatoren:

**Windows / Visual Studio**

- `Visual Studio 17 2022`
- `Visual Studio 16 2019`
- `Visual Studio 15 2017`
- (ältere: 14 2015, 12 2013, …)
- Zusatz-Option `-A` für Architektur, z. B. `-A x64` oder `-A Win32`

**Makefile-basiert**

- `Unix Makefiles` – Standard unter Linux/macOS
- `MinGW Makefiles` – Windows mit MinGW/GCC
- `NMake Makefiles` – Windows mit Microsofts NMake (MSVC-Toolchain, ohne VS-IDE)
- `MSYS Makefiles`

**Ninja**

- `Ninja` – schneller, einfacher Build-Generator, plattformübergreifend, oft schneller als Make
- `Ninja Multi-Config` – wie Ninja, aber mit mehreren Konfigurationen (Debug/Release) gleichzeitig, wie bei Visual Studio

**Xcode (macOS)**

- `Xcode`

**Weitere / spezialisiert**

- `CodeBlocks - Unix Makefiles` / `CodeBlocks - Ninja` – für die Code::Blocks-IDE
- `CodeLite - ...`
- `Eclipse CDT4 - ...`
- `Sublime Text 2 - ...`
- `Kate - ...`
- `Watcom WMake`
- `Green Hills MULTI`

**Befehl zur Anzeige installierter Generatoren:**

```
cmake --help
```

zeigt am Ende alle auf dem System verfügbaren Generatoren an.

**Hinweis:** Manche Generatoren sind "single-config" (Make, Ninja – Konfiguration wird bei `cmake -G` per `-DCMAKE_BUILD_TYPE=Release` festgelegt), andere "multi-config" (Visual Studio, Xcode, Ninja Multi-Config – Konfiguration wird erst beim Build mit `--config Release` gewählt).


### Kurzer Vergleich der vier auf Windows nutzbaren Generatoren:

**Visual Studio 17 2022**

- Erzeugt `.sln`/`.vcxproj`-Dateien
- Nutzt den MSVC-Compiler (`cl.exe`)
- Multi-Config (Debug/Release wählbar beim Build mit `--config`)
- IDE-Integration, Debugging direkt in Visual Studio möglich
- Baut standardmäßig alle Konfigurationen langsamer als Ninja (mehr Overhead)

**Unix Makefiles**

- Erzeugt klassische `Makefile`s
- Braucht i. d. R. trotzdem MSVC als Compiler, wenn du aus der "Developer Command Prompt" arbeitest – oder GCC, falls installiert (z. B. über MSYS2/Cygwin)
- Single-Config: `CMAKE_BUILD_TYPE` muss beim Konfigurieren gesetzt werden (`-DCMAKE_BUILD_TYPE=Release`)
- Eigentlich für Unix gedacht, funktioniert unter Windows nur mit passendem `make`-Tool im PATH

**MinGW Makefiles**

- Wie oben, aber explizit für den MinGW-GCC-Compiler gedacht
- Erzeugt `.exe` ohne Abhängigkeit von MSVC – nutzt GCC/G++ und `mingw32-make`
- Single-Config
- Ergebnis-Binaries können sich in ABI/Runtime-Verhalten von MSVC-Builds unterscheiden (z. B. andere C-Runtime, andere Exception-Handling-Mechanismen)

**Ninja**

- Erzeugt `build.ninja`-Dateien
- Compiler ist unabhängig wählbar (MSVC oder GCC/Clang, je nach Umgebung/PATH bzw. `-DCMAKE_C_COMPILER=...`)
- Single-Config (außer `Ninja Multi-Config`)
- Deutlich schneller beim Parallel-Build als Make oder MSBuild, minimaler Overhead
- Wird von vielen IDEs (CLion, VS Code) bevorzugt, da schnelles inkrementelles Bauen

**Praktischer Unterschied im Ergebnis** Alle vier erzeugen lauffähige `.exe`, weil sie letztlich denselben Compiler ansteuern können (meistens MSVC, wenn du nichts anderes konfiguriert hast). Der Unterschied liegt in:

- Build-Geschwindigkeit (Ninja meist am schnellsten)
- Config-Handling (VS/Ninja-Multi-Config = flexibel zur Build-Zeit, Make/Ninja = fix beim Konfigurieren)
- Tooling/IDE-Anbindung (VS = beste IDE-Integration)
- Tatsächlich verwendetem Compiler (MSVC vs. GCC), was bei Low-Level-Code (Threading, Exceptions, Name Mangling) relevant werden kann

Möchtest du wissen, wie du gezielt prüfst, welcher Compiler bei welchem Generator tatsächlich verwendet wurde?

### So prüfst du den tatsächlich verwendeten Compiler:

**1. Direkt aus dem CMake-Output beim Konfigurieren** Beim Ausführen von `cmake -G "..." ..` zeigt CMake in den ersten Zeilen an:

```
-- The C compiler identification is MSVC 19.38.33130.0
-- The CXX compiler identification is GNU 13.2.0
```

Das steht direkt im Terminal – einfach nach oben scrollen oder Output in eine Datei umleiten:

```
cmake -G "Ninja" .. > config_log.txt 2>&1
```

**2. Aus dem CMakeCache.txt** Nach dem Konfigurieren liegt im Build-Verzeichnis eine `CMakeCache.txt`. Darin suchen nach:

```
CMAKE_C_COMPILER:FILEPATH=...
CMAKE_CXX_COMPILER:FILEPATH=...
```

Das zeigt den vollständigen Pfad zum tatsächlich verwendeten Compiler, z. B.:

- `C:/Program Files/Microsoft Visual Studio/2022/.../cl.exe` (MSVC)
- `C:/msys64/mingw64/bin/gcc.exe` (MinGW)

**3. Per Kommando in der PowerShell/CMD**

```
findstr "CMAKE_CXX_COMPILER:" CMakeCache.txt
```

**4. Compiler-Version direkt aus der .exe prüfen (nachträglich)** Mit `dumpbin` (kommt mit Visual Studio):

```
dumpbin /headers deine_exe.exe | findstr "machine"
```

zeigt Zielarchitektur (x86/x64). Für genauere Herkunft (MSVC vs. MinGW) hilft:

```
dumpbin /dependents deine_exe.exe
```

- MSVC-Programme hängen typischerweise von `VCRUNTIME140.dll`, `MSVCP140.dll` ab
- MinGW-Programme hängen von `libgcc_s_seh-1.dll`, `libstdc++-6.dll`, `libwinpthread-1.dll` ab (falls nicht statisch gelinkt)

**Praktischer Tipp:** Wenn du sichergehen willst, welchen Compiler ein Generator nimmt, kannst du ihn auch explizit vorgeben statt CMake raten zu lassen:

```
cmake -G "Ninja" -DCMAKE_C_COMPILER=cl -DCMAKE_CXX_COMPILER=cl ..
```

oder für MinGW:

```
cmake -G "Ninja" -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ ..
```