from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class MyAppConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires("segger-rtt/8.58.0")
        #self.requires("segger-rtt/7.54")

    #def build_requirements(self):
    #    self.tool_requires("cmake/3.23.5")
        
    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
