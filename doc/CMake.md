Kurz: **CMake ist weder Build-System – noch Build-Tool, genauer gesagt**. CMake ist ein **Build-System-Generator** (auch "Meta-Build-System" genannt). Eine eigene Kategorie.

**Die drei Ebenen sauber getrennt:**

|Ebene|Beispiel|Aufgabe|
|---|---|---|
|**1. Build-System-Generator**|**CMake**|Liest plattformunabhängige Projektbeschreibung (`CMakeLists.txt`), erzeugt daraus Konfigurationsdateien für ein Build-Tool|
|**2. Build-Tool**|`make`, `ninja`, `MSBuild`|Liest die generierten Dateien (`Makefile`, `build.ninja`, `.vcxproj`), steuert den eigentlichen Build-Prozess (Reihenfolge, Parallelität, was neu gebaut werden muss)|
|**3. Compiler/Linker**|`cl.exe`, `gcc`, `clang`|Übersetzt tatsächlich Quellcode in Maschinencode, linkt zu `.exe`/`.dll`|

**CMake selbst kompiliert nichts.** Es kennt keinen einzigen Compiler-Befehl im eigentlichen Sinn – es erzeugt nur die Datei, die einem anderen Tool sagt, _wie_ zu kompilieren ist.

**Warum die Unterscheidung "Build-System" vs. "Build-Tool" oft verschwimmt:** Umgangssprachlich wird "Build-System" manchmal für Ebene 2 genutzt (also: "make ist ein Build-System"), manchmal als Oberbegriff für den ganzen Prozess. Es gibt da keine 100% scharfe, allgemein genormte Terminologie – aber im CMake-Kontext ist die Unterscheidung wichtig:

- **CMake** = Generator (Ebene 1)
- **Make/Ninja/MSBuild** = das tatsächliche Build-Tool/Build-System (Ebene 2)

**Analogie:** CMake ist wie ein Architekt, der je nach Land (Windows/Linux/Mac) einen passenden Bauplan (Makefile/Ninja-Datei/VS-Projekt) für die lokale Baufirma (make/ninja/MSBuild) erstellt. Der Architekt selbst legt keinen Ziegelstein – das macht die Baufirma, die den Plan umsetzt.

Deshalb der zweistufige Ablauf bei dir:

```
cmake -G "..." ..      # Schritt 1: Architekt erstellt Bauplan
cmake --build .         # Schritt 2: ruft Baufirma auf, die nach Plan baut
```

