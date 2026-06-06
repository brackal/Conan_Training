from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class RecipeForWellDoneApplication(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires("fmt/10.2.1")

    #def build_requirements(self):
    #    self.tool_requires("cmake/3.23.5")
        
    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

