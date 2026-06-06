# Paketmanager – Was ist das?
Ein Paketmanager ist ein Werkzeug, das die Installation, Aktualisierung, Konfiguration und Entfernung von Software-Paketen (Bibliotheken, Frameworks, Tools) automatisiert. Anstatt Abhängigkeiten manuell herunterzuladen und zu verknüpfen, übernimmt der Paketmanager all das mit einem einzigen Befehl.
## Was macht ein Paketmanager genau?
Ein Paketmanager übernimmt typischerweise folgende Aufgaben:
1. **Abhängigkeitsverwaltung (Dependency Management):** Er erkennt automatisch, welche anderen Pakete ein Paket benötigt (Abhängigkeiten/Dependencies), und installiert diese rekursiv mit.
2. **Versionskontrolle:** Er stellt sicher, dass kompatible Versionen installiert werden (z. B. lodash >= 4.0.0), und verhindert Versionskonflikte.
3. **Zentrales Repository:** Pakete werden aus einem zentralen Register (Registry) heruntergeladen, z. B. npmjs.com oder pypi.org.
4. **Installation / Deinstallation:** Ein einziger Befehl (npm install, pip install, ...) reicht, um ein Paket projektlokal oder systemweit zu installieren.
5. **Lock-Files:** Viele Paketmanager erzeugen eine Lock-Datei (package-lock.json, Pipfile.lock), die exakte Versionen einfriert – für reproduzierbare Builds im Team.
6. **Skripte & Lifecycle-Hooks:** Paketmanager können Build-Skripte, Tests oder andere Automatisierungen ausführen.


# Kernkonzepte
## Pakete (Recipes)
Jedes Paket wird durch eine conanfile.py (oder conanfile.txt) beschrieben. Darin stehen Abhängigkeiten, Build-Optionen und Metadaten.
#### conanfile.txt
[requires]
fmt/10.2.1
nlohmann_json/3.11.3

[generators]
CMakeDeps
CMakeToolchain

## Profile
siehe ConanProfiles/readme.md

## Typischer Workflow
#### 1. conanfile.txt definieren
Hier müssen notwendige Pakete, Generatoren und weitere Definitionen festgelegt werden
#### 2. CMakeLists.txt definieren
Prüfen ob in CMakeLists.txt notwendige Pakete verlinkt sind
#### 3. Standardprofil erstellen
conan profile detect
#### 4. Abhängigkeiten installieren
conan install . --output-folder=build --build=missing
#### 5. Projekt bauen (z. B. mit CMake)
cmake -B build -DCMAKE_TOOLCHAIN_FILE=build/conan_toolchain.cmake
cmake --build build


# conanfile.txt
## Was machen CMakeDeps und CMakeToolchain?
Diese beiden Generatoren sind die Brücke zwischen Conan und CMake. Conan kennt die Pakete, CMake kennt sie nicht – die Generatoren übersetzen das Wissen von Conan in Dateien, die CMake versteht.

#### CMakeDeps – „Wo sind die Pakete?"
CMakeDeps generiert CMake-Konfigurationsdateien (z. B. Find\<Paket\>.cmake bzw. \<Paket\>Config.cmake) für alle deine Conan-Abhängigkeiten. Damit kann CMake die Pakete per find_package() finden, ohne dass du die Pfade manuell angeben musst.

#### CMakeToolchain – „Wie wird gebaut?"
CMakeToolchain generiert eine CMake-Toolchain-Datei (conan_toolchain.cmake), die Build-Einstellungen wie Compiler, Architektur, Build-Typ (Debug/Release) usw. an CMake weitergibt. conan_toolchain.cmake teilt CMake alles mit, was Conan über deine Build-Umgebung weiß. 
CMake weiß standardmäßig nichts von Conan. Mit:
cmake .. -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake
sagst du CMake: „Lies zuerst diese Datei, bevor du irgendetwas konfigurierst."
Dadurch findet find_package(fmt REQUIRED) die von Conan installierten Pakete.

**Zusammengefasst:** Dein Projekt nutzt Conan als Paketmanager zusammen mit CMake als Build-System. Nach einem conan install . werden diese beiden Dateien erzeugt, sodass CMake automatisch weiß, wo die Abhängigkeiten liegen und wie gebaut werden soll.


# CMakeLists.txt
Prüfen ob in CMakeLists.txt notwendige Pakete verlinkt sind. Z.B.
find_package(fmt REQUIRED)
target_link_libraries(MyTarget fmt::fmt)


# Abhängigkeiten installieren
## Was bedeutet „Paketmanager installiert Pakete"?
Installation = Diese Schritte passieren im Hintergrund
conan install .   /   pip install numpy   /   vcpkg install boost
        │
        ▼
┌───────────────────────────────────────────────────┐
│  1. Auflösen       Was brauche ich überhaupt?                     │
│  2. Herunterladen  Dateien vom Internet holen                  │
│  3. Entpacken      Archiv (.zip/.tar.gz) entpacken                 │
│  4. Kompilieren    (nur bei Source-Paketen, z.B. C/C++)     │
│  5. Ablegen        Dateien an den richtigen Ort kopieren     │
│  6. Verknüpfen     Dem Build-System sagen wo alles liegt  │
└───────────────────────────────────────────────────┘

1️⃣ Auflösen (Dependency Resolution)
Bevor irgendetwas heruntergeladen wird, prüft der Paketmanager:
- Welche Version des Pakets passt zu meinen Anforderungen?
- Hat dieses Paket selbst noch Abhängigkeiten?
- Gibt es Versionskonflikte?

2️⃣ Herunterladen
Der Paketmanager lädt die Paket-Dateien von der Registry herunter.
Diese Dateien sind entweder:
- Binaries (vorkompiliert, sofort nutzbar)
- Source-Code (muss noch kompiliert werden → Schritt 4)

3️⃣ Entpacken
Das heruntergeladene Archiv wird entpackt. 

4️⃣ Kompilieren (nur bei C/C++ aus Source)
Bei Sprachen wie Python/JS sind Pakete meist reiner Code → kein Kompilieren nötig.
Bei C/C++ (z.B. Conan, vcpkg) wird oft aus dem Quellcode kompiliert.

5️⃣ Ablegen (wo landen die Dateien?)
Die Dateien werden in einen lokalen Cache kopiert – nicht in dein Projektverzeichnis.

6️⃣ Verknüpfen (dem Build-System Bescheid geben)
Das ist der entscheidende letzte Schritt. Dein Compiler muss wissen:
- Wo liegen die Header-Dateien? (-I /pfad/zu/include)
- Wo liegen die kompilierten Libs? (-L /pfad/zu/lib)
- Welche Libs soll er einbinden? (-lboost_system)

## Der Unterschied: Statisch vs. Dynamisch
Wenn eine Bibliothek „installiert" wird, gibt es zwei Varianten:
Statisch (.a / .lib) **vs.** Dynamisch (.so / .dll)
Was passiert: Lib-Code wird in deine .exe hineinkopiert **vs.** Lib bleibt separat, wird zur Laufzeit geladen
Ergebnis: Eine große, eigenständige .exe **vs.** Kleine .exe + separate Lib-Datei
Vorteil: Keine Abhängigkeiten zur Laufzeit **vs.** Mehrere Programme teilen sich eine Lib
Nachteil: Größere Binary **vs.** Lib muss auf Zielrechner vorhanden sein

#### Zusammenfassung in einem Satz
„Installieren" bedeutet: Paketmanager lädt die richtigen Dateien (Header + kompilierte Lib) herunter, legt sie in einen Cache, und sorgt dafür, dass dein Compiler sie findet – alles automatisch, ohne dass du manuell Pfade setzen oder Quellcode kompilieren musst.



# Conan commands
#### Alle Profile anzeigen
conan profile list

#### Alle Pakete anzeigen
conan list "\*"

#### Alle Pakete löschen
conan remove "\*" -c

#### Ein bestimmtes Paket löschen
conan remove "boost/\*" -f

#### Eine bestimmte Version löschen
conan remove "boost/1.79.0" -f

#### Die Standard-Einstellung der Umgebung für Conan Profil ermitteln 
conan profile detect --force

#### Verisonen prüfen
python --version
conan --version
cmake --version
make --version
./arm-none-eabi-gcc --version
ninja --version

#### Wo liegt der MSVC Compiler?
C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.38.33130\bin\Hostx64\x64
./cl.exe --version
Microsoft (R) C/C++-Optimierungscompiler Version 19.38.33133 für x64
Copyright (C) Microsoft Corporation. Alle Rechte vorbehalten.

19.3x.xxxxx -> compiler.version=193 in Conan Profile

# Ergänzungen
https://docs.conan.io/2/tutorial.html

#### Was ist ein Build Environment?
Das Build Environment ist die Menge aller Umgebungsvariablen und Werkzeuge, die während des Kompiliervorgangs aktiv sind.
#### Umgebungsvariablen – was ist das?
Das Betriebssystem stellt jedem Prozess eine Liste von Schlüssel-Wert-Paaren zur Verfügung. Auf einem Linux-System z.B.:
echo $CC        → /usr/bin/gcc
echo $CXX       → /usr/bin/g++
echo $PATH      → /usr/bin:/usr/local/bin:...

#### Warum ist das für den Build wichtig?
Wenn CMake startet, schaut es als erstes in diese Umgebungsvariablen:

CMake startet
    │
    ├─ Ist $CC gesetzt?   → benutze diesen C-Compiler
    ├─ Ist $CXX gesetzt?  → benutze diesen C++-Compiler
    ├─ Ist $LD gesetzt?   → benutze diesen Linker
    └─ Nichts gesetzt?    → benutze System-Standard (z.B. /usr/bin/gcc)