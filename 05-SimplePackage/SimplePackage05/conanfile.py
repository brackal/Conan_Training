from conan import ConanFile
from conan.tools.layout import basic_layout
from conan.tools.files import get, copy
import os

class RecipeForWellDoneApplication(ConanFile):
    name = "segger-rtt"
    #version = "8.58.0"
    version = "7.54"
    package_type = "static-library"
    settings = "os", "arch"
    #options = {"shared": [True, False], "fPIC": [True, False]}
    #default_options = {"shared": False, "fPIC": True}

    #exports_sources = "CMakeLists.txt", "src/*"
    #exports_sources = "CMakeLists.txt"

    def source(self):
        get(
            self,
            #url="https://github.com/SEGGERMicro/RTT/archive/refs/tags/V8.58.0.tar.gz",
            #sha256="0857012c1d26c90a55e6c2b0a730e039715a9ab9ab0a57c83dcf15f41b878932",
            url="https://github.com/SEGGERMicro/RTT/archive/refs/tags/V7.54.tar.gz",
            sha256="b7cab04f106cb40a6a5c00624fc98100798196e46346345f4e4b04627ea7f3e3",
            strip_root=True,
        )

    def layout(self):
        basic_layout(self)

    def package(self):
        # Alle .c und .h aus RTT/ kopieren
        copy(self, "*.c",
             src=os.path.join(self.source_folder, "RTT"),
             dst=os.path.join(self.package_folder, "src"),
             keep_path=False)
        copy(self, "*.h",
             src=os.path.join(self.source_folder, "RTT"),
             dst=os.path.join(self.package_folder, "include"),
             keep_path=False)

        # Config-Header dazu
        copy(self, "*.h",
             src=os.path.join(self.source_folder, "Config"),
             dst=os.path.join(self.package_folder, "include"),
             keep_path=False)

    def package_info(self):
        # Keine "libs", da keine Bibliothek gebaut wird
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.srcdirs = ["src"]      # Conan-Konvention für "hier liegen Quell-Dateien"
