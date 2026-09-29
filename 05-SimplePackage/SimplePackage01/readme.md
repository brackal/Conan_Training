# Using simple Conan:
you are here: 05-SimplePackage/SimplePackage01

The directory SimplePackage01 contains only readme.md

#### Use the conan new command to create a “Hello World” C++ library example project:
conan new cmake_lib -d name=hello -d version=1.0

#### Let’s build the package from sources with the current default configuration, and then let the test_package folder test the package:
conan create .

Usage of library see example 06-SimpleUsingSimplePackage01.