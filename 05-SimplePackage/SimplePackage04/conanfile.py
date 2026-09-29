from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import get, copy
import os

class RecipeForWellDoneApplication(ConanFile):
    name = "segger-rtt"
    version = "8.58.0"
    #version = "7.54"
    package_type = "static-library"
    description = "<Description of segger-rtt package here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    #exports_sources = "CMakeLists.txt", "src/*"
    exports_sources = "CMakeLists.txt"

    def source(self):
        get(
            self,
            url="https://github.com/SEGGERMicro/RTT/archive/refs/tags/V8.58.0.tar.gz",
            sha256="0857012c1d26c90a55e6c2b0a730e039715a9ab9ab0a57c83dcf15f41b878932",
            #url="https://github.com/SEGGERMicro/RTT/archive/refs/tags/V7.54.tar.gz",
            #sha256="b7cab04f106cb40a6a5c00624fc98100798196e46346345f4e4b04627ea7f3e3",
            strip_root=True,
        )

    def config_options(self):
        if self.settings.os in ("Windows", "baremetal"):
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.cache_variables["SEGGER_SOURCE_DIR"] = self.source_folder.replace("\\", "/")
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        # Header direkt aus dem Source-Folder ins Package kopieren
        copy(self, "*.h",
            src=os.path.join(self.source_folder, "RTT"),
            dst=os.path.join(self.package_folder, "include"),
            keep_path=False)

        # Header aus Config/ (insbesondere SEGGER_RTT_Conf.h)
        copy(self, "*.h",
             src=os.path.join(self.source_folder, "Config"),
             dst=os.path.join(self.package_folder, "include"),
             keep_path=False)
        
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["segger-rtt"]