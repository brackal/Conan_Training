
## 1. Das Profil (Profile) – die Hauptquelle

Ein Conan-Profil ist eine Textdatei, die eine Ziel-Konfiguration beschreibt: `os`, `arch`, `compiler` (inkl. Version, `libcxx`, `cppstd`), `build_type`, plus optional `conf`- und `buildenv`-Einträge.

Zweck:

- Liefert die konkreten Werte für die in `settings = ...` deklarierten Kategorien.
- Bestimmt damit, welches Binärpaket Conan sucht/lädt bzw. baut.
- Fließt in die generierten Dateien (z. B. `conan_toolchain.cmake`) ein, die dann von CMake für den eigentlichen Build verwendet werden.

Kurz: Es ist die zentrale Konfigurationsquelle, mit der Conan festlegt, für welche Plattform/welchen Compiler/welchen Build-Type die Abhängigkeiten aufgelöst und die Build-Dateien erzeugt werden.





**Conan selbst kompiliert keinen Code.** Das Profil beschreibt die Ziel-Konfiguration (Compiler, Architektur, Build-Type), die für zwei Zwecke verwendet wird:

1. **Binärpaket-Auswahl**: Anhand dieser Werte berechnet Conan eine Paket-ID (Hash) und sucht/lädt das passende, bereits kompilierte Binärpaket aus dem Cache/Remote.
    
2. **Datei-Generierung**: Diese Werte fließen in `conan_toolchain.cmake` ein – die tatsächliche Kompilierung übernimmt dann CMake/das Build-Tool (Make, Ninja, MSBuild), wenn du `cmake --build .` ausführst.
    

**Ausnahme**: Wenn Conan ein Paket aus Quellcode bauen muss (z. B. bei `--build=missing`), ruft Conan intern zwar Build-Tools auf (über Helper-Klassen wie `CMake(self)` in der `build()`-Methode des jeweiligen Pakets) – aber auch dann kompiliert nicht Conan selbst, sondern Conan orchestriert/ruft den externen Compiler/Build-Tool auf.

Zusammengefasst: Das Profil beschreibt die Zielkonfiguration, mit der **gebaut werden soll** (im Sinne von: später gebaut wird) – nicht, dass Conan selbst diesen Bauvorgang durchführt.




Der wichtigste Input für **conan_toolchain.cmake** ist das **Conan-Profil**, eine Textdatei, die beschreibt, mit welchem Compiler, welcher Architektur, welchem Build-Type usw. gebaut werden soll.

Standardmäßig liegt es unter:

```
~/.conan2/profiles/default
```

Und sieht z. B. so aus:

```ini
[settings]
os=Linux
arch=x86_64
compiler=gcc
compiler.version=13
compiler.libcxx=libstdc++11
compiler.cppstd=17
build_type=Release

[buildenv]
...

[conf]
tools.build:jobs=8
```

Dieses Profil wird beim `conan install` automatisch benutzt, wenn du nichts anderes angibst. Du kannst es aber explizit wählen:

```bash
conan install . -pr=meinprofil
```

Woher kommt das Default-Profil überhaupt? Beim ersten `conan profile detect` (oder automatisch beim ersten Conan-Aufruf) erkennt Conan deinen installierten Compiler, dein Betriebssystem etc. und legt daraus ein Startprofil an.

## 2. Zwei Profile: `host` und `build`

Conan unterscheidet zwischen:

- **build profile** (`-pr:b`) – die Maschine, auf der _kompiliert_ wird
- **host profile** (`-pr:h`) – die Maschine, für die das Ergebnis _laufen_ soll

Bei normalem Bauen (kein Cross-Compiling) sind beide identisch. Bei Cross-Compiling (z. B. für ARM-Embedded von einem x86-Rechner aus) unterscheiden sie sich – und genau diese Trennung fließt in die `conan_toolchain.cmake` ein (z. B. `CMAKE_SYSTEM_NAME`, `CMAKE_SYSTEM_PROCESSOR` für Cross-Compiling).

## 3. Die `conanfile.py` selbst

Attribute in der Rezeptdatei können Settings/Optionen beeinflussen oder einschränken, z. B.:

```python
class MyProjectConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
```

Auch Methoden wie `configure()` oder `generate()` können programmatisch Werte setzen oder anpassen – z. B.:

```python
def generate(self):
    tc = CMakeToolchain(self)
    tc.variables["MY_CUSTOM_FLAG"] = "ON"
    tc.generate()
```

## 4. Kommandozeilen-Overrides

Du kannst beim Aufruf einzelne Settings/Options direkt überschreiben, ohne das Profil zu ändern:

```bash
conan install . -s build_type=Debug -s compiler.cppstd=20 -o shared=True
```

Diese haben höchste Priorität.

## 5. `[conf]`-Einträge (Konfigurationsvariablen)

Zusätzlich zu `settings` gibt es `conf`-Werte (z. B. `tools.cmake.cmaketoolchain:generator=Ninja`), die steuern, _wie_ der Generator arbeitet – etwa welchen CMake-Generator (Ninja/Make/Visual Studio) er erzeugt. Diese kommen ebenfalls aus dem Profil oder per `-c` auf der Kommandozeile.

## Zusammengefasst – die Priorität (niedrig → hoch):

1. Defaults im Rezept (`conanfile.py`)
2. Profil-Datei (`settings`, `options`, `conf`, `buildenv`)
3. Kommandozeilen-Argumente (`-s`, `-o`, `-c`)

Conan führt das alles zusammen zu einem finalen Satz an Settings, und genau **dieser finale, aufgelöste Zustand** wird dann in `conan_toolchain.cmake` geschrieben – als CMake-Variablen, die dein Build direkt nutzen kann.


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
Setting                                  Bedeutung                       Beispielwerte
os                                          Zielbetriebssystem          Windows, Linux, Macos
arch                                      CPU-Architektur               x86_64, x86, armv8
build_type                            Debug oder Release         Debug, Release
compiler                              Compiler-Toolchain           msvc, gcc, clang
compiler.version                  Version des Compilers       193 (MSVC 2022)
compiler.cppstd                  C++-Sprachstandard          14, 17, 20, 23
compiler.runtime                Runtime-Linking                 dynamic, static
compiler.runtime_type        Runtime-Variante              Debug, Release

Diese Kombination ergibt zusammen eine eindeutige Paket-ID (den sogenannten Package-Hash). Conan berechnet daraus einen Hash und sucht damit das passende vorkompilierte Binary.

os=Windows + arch=x86_64 + compiler=msvc + ... → bed280a9c51d41820ca64294cf373083ad852aa8
Ändert sich ein einziger Wert → anderer Hash → anderes Binary wird gesucht.


- compiler.cppstd=14 → Das gibt an, welchen C++-Sprachstandard Conan beim Bauen von Paketen verwenden soll, in diesem Fall C++14 (erschienen 2014).
- compiler.version → die MSVC/GCC/Clang-Toolchain-Version (z.B. 193 = MSVC 2022)
- compiler.runtime → ob die C++-Runtime statisch oder dynamisch gelinkt wird (static/dynamic)

[[Conan Settings]]