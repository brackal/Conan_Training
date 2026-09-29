from conan import ConanFile
from conan.tools.files import copy
#from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout
import os

class MyAppConan(ConanFile):
    requires = "hello-library/1.0.0"
    #generators = "CMakeToolchain", "CMakeDeps"
    #settings = "os", "compiler", "build_type", "arch"

    def generate(self):
        # make libs/ directory if not exists
        libs_dir = os.path.join(self.source_folder, "libs")
        os.makedirs(libs_dir, exist_ok=True)

        # copy files from src/directory of package into libs/ directory of consumer project
        for dep in self.dependencies.values():
            copy(self, "**/*.h",
                 src=dep.package_folder,
                 dst=libs_dir)
            copy(self, "**/*.cpp",
                 src=dep.package_folder,
                 dst=libs_dir)
