Kurz erklärt:

**Build-System (Definition):** Ein Build-System ist der **Gesamtprozess bzw. das Regelwerk**, das festlegt, _wie_ aus Quellcode ein fertiges Programm entsteht – also: welche Dateien wovon abhängen, in welcher Reihenfolge sie verarbeitet werden müssen, welche Befehle dafür nötig sind, und was bei einer Änderung neu gebaut werden muss.

Ein Build-System ist damit zunächst **kein Programm**, sondern ein **Konzept/eine Spezifikation** – vergleichbar mit einem Kochrezept: die Beschreibung, was in welcher Reihenfolge zu tun ist.

**Build-Tool (Definition):** Ein Build-Tool ist das **ausführbare Programm**, das ein Build-System (also das Rezept) tatsächlich _ausführt_ – die Befehle abarbeitet, Dateien liest/schreibt, den Compiler aufruft usw.

**Konkret angewendet:**

|Begriff|Was es ist|Beispiel|
|---|---|---|
|**Build-System**|Die _Beschreibung/Regeln_, was gebaut wird und wie (Abhängigkeitsgraph, Befehle)|Der Inhalt einer `Makefile` oder `build.ninja`|
|**Build-Tool**|Das _Programm_, das diese Beschreibung liest und ausführt|`make`, `ninja`, `MSBuild.exe`|


**Wo CMake einzuordnen ist:** CMake erzeugt weder das eine noch führt es das andere direkt aus. Es ist ein **Generator**, der aus einer abstrakten Beschreibung (`CMakeLists.txt`) ein konkretes Build-System (z. B. eine `Makefile` mit allen Regeln) erzeugt – dieses wird dann von einem Build-Tool (`make`) ausgeführt.

```
CMakeLists.txt          →  CMake (Generator)  →  Makefile (= Build-System, das Regelwerk)
                                                        ↓
                                                  make (= Build-Tool, führt es aus)
                                                        ↓
                                                  .exe (Ergebnis)
```


**Beispiele, was ein "Build-System" hier konkret ist:**

|Generator|erzeugte Dateien|tatsächliches Build-Tool, das kompiliert|
|---|---|---|
|`Unix Makefiles`|`Makefile`|`make`|
|`MinGW Makefiles`|`Makefile`|`mingw32-make`|
|`Ninja`|`build.ninja`|`ninja`|
|`Visual Studio 17 2022`|`.sln`, `.vcxproj`|`MSBuild.exe` (oder Visual-Studio-IDE)|

Jedes dieser Tools (`make`, `ninja`, `MSBuild`) hat sein eigenes Dateiformat, eigene Syntax, eigene Regeln, wie es Abhängigkeiten trackt und parallel baut. Das sind die eigentlichen "Build-Systeme".

**Warum das Zwischenschritt-Prinzip sinnvoll ist:** Du schreibst deine `CMakeLists.txt` **einmal**, plattform- und tool-unabhängig. Je nachdem, welchen Generator du wählst, erzeugt CMake daraus passende Dateien für das gewünschte Build-Tool – ohne dass du deine Projektbeschreibung ändern musst.

`cmake --build .` ist dann nur ein Wrapper, der automatisch das richtige Tool aufruft (`make`, `ninja` oder `msbuild`, je nachdem was im Verzeichnis liegt) – du musst dich nicht merken, welcher Befehl für welchen Generator zuständig ist.