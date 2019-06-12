from conans import ConanFile, CMake, tools


class Cli11Conan(ConanFile):
    name = "CLI11"
    version = "1.8.0"
    license = "BSD-3-Clause"
    url = "https://cliutils.gitlab.io/"
    description = "Command line parser for C++11"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake_find_package"
    exports_sources = "*"

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/CLIUtils/CLI11.git", "v" + self.version)

    def build(self):
        pass

    def package(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_TESTING"] = "OFF"
        cmake.definitions["CLI11_EXAMPLES"] = "OFF"
        cmake.configure()
        cmake.install()

    def package_info(self):
        self.info.header_only()
