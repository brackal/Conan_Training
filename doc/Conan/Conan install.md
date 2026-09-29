`conan install .` ist der Befehl, mit dem Conan (der C/C++-Paketmanager) die Abhängigkeiten eines Projekts auflöst und für den Build vorbereitet. Im Detail passiert dabei Folgendes:

## 1. Rezept finden

Conan sucht im aktuellen Verzeichnis (`.`) nach einer `conanfile.txt` oder `conanfile.py`, die die Abhängigkeiten des Projekts beschreibt.

## 2. Dependency-Graph auflösen

Conan liest die dort gelisteten Requirements (z. B. `boost/1.84.0`, `fmt/10.2.1`) und baut daraus einen vollständigen Abhängigkeitsgraphen – inklusive transitiver Abhängigkeiten (Abhängigkeiten von Abhängigkeiten).

## 3. Binärpakete suchen/bauen

Für jede Abhängigkeit prüft Conan:

- Ist das passende Binärpaket (für deine Plattform, deinen Compiler, dein Build-Type – Debug/Release usw.) schon im lokalen Cache (`~/.conan2/p` bzw. früher `~/.conan/data`)?
- Falls nicht: Ist es in einem konfigurierten Remote (z. B. ConanCenter) verfügbar? Dann wird es heruntergeladen.
- Falls kein passendes Binary existiert und `--build` nicht anders angegeben ist, bricht Conan mit einem Hinweis ab ("missing binary") – man muss dann z. B. `conan install . --build=missing` verwenden, damit fehlende Pakete aus dem Quellcode gebaut werden.

## 4. Generator-Dateien erzeugen

Das ist oft der eigentlich wichtige Teil: Conan erzeugt im Zielverzeichnis Dateien, die dein Build-System (CMake, Meson, MSBuild, Makefiles …) versteht, z. B.:

- `conan_toolchain.cmake`
- `CMakeDeps`-Dateien (`fmt-config.cmake` usw.)
- `conanbuildinfo.txt` (bei älteren Generatoren)

Diese Dateien enthalten Include-Pfade, Bibliothekspfade, Compiler-Flags usw., damit dein Build-System die Conan-Pakete findet.

## 5. Optional: Environment-Skripte

Falls nötig, erzeugt Conan auch Skripte wie `conanrun.sh`/`conanbuild.sh`, um zur Laufzeit oder beim Bauen Umgebungsvariablen (PATH, LD_LIBRARY_PATH etc.) korrekt zu setzen.

## Typische Zusatz-Optionen

- `--build=missing` – fehlende Binärpakete selbst bauen
- `-s build_type=Debug` – Build-Type festlegen
- `-pr=default` – ein bestimmtes Profil verwenden (Compiler, Architektur, Standard-Library …)
- `-of=build` – Output-Verzeichnis für die generierten Dateien festlegen

Kurz gesagt: `conan install .` sorgt dafür, dass alle benötigten Bibliotheken verfügbar sind und dein Build-System (z. B. CMake) weiß, wo es sie findet – ohne dass du das manuell konfigurieren musst.


[[Conan Generators]] [[Conan generate()]]