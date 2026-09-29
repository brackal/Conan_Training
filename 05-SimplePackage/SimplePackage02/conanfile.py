from conan import ConanFile
from conan.tools.files import copy
import os

class HelloLibrary(ConanFile):
    name = "hello-library"
    version = "1.0.0"
    package_type = "header-library"  # ← wichtig! kein Binary nötig
    settings = ()                     # ← keine Compiler/OS Settings

    # ** = rekursiv alle Unterordner
    exports_sources = "**/*.h", "**/*.cpp"

    def package(self):
        # Alles rekursiv vom source root kopieren
        copy(self, "**/*.h",
         src=os.path.join(self.source_folder, "src"),  # src/ als Basis
         dst=self.package_folder)                        # direkt in package root
        copy(self, "**/*.cpp",
         src=os.path.join(self.source_folder, "src"),  # src/ wird weggeschnitten
         dst=self.package_folder)

    def package_info(self):
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
        # Root als include-Basis, alle Unterordner erreichbar
        self.cpp_info.includedirs = ["."]
        self.cpp_info.srcdirs = ["."]
