from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout


class MyAppConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    #generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        #self.requires("segger-rtt/1.0")
        #self.requires("segger-rtt/8.58.0")
        self.requires("segger-rtt/7.54")

    #def build_requirements(self):
    #    self.tool_requires("cmake/3.23.5")
    
    
    def generate(self):
        self.output.warning(">>>>>>>>>> GENERATE WIRD AUSGEFÜHRT <<<<<<<<<<")
        tc = CMakeToolchain(self)
        segger_dep = self.dependencies["segger-rtt"]
        self.output.info(f"segger srcdirs = {segger_dep.cpp_info.srcdirs}")
        segger_src = segger_dep.cpp_info.srcdirs[0]
        tc.cache_variables["SEGGER_SRC_DIR"] = segger_src.replace("\\", "/")
        self.output.warning(f">>>>>>>>>> SEGGER_SRC_DIR gesetzt auf: {segger_src} <<<<<<<<<<")
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
