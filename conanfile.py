from conan import ConanFile
from conan.tools.files import copy
import os


class STM32CubeH7Conan(ConanFile):
    name = "stm32cubeh7"
    version = "1.1.0"
    license = "BSD-3-Clause"
    description = "STM32CubeH7 HAL Driver + CMSIS sources and headers"
    url = "https://github.com/Gastronomous-Technologies/STM32CubeH7"
    no_copy_source = True
    exports_sources = (
        "Drivers/STM32H7xx_HAL_Driver/Src/*",
        "Drivers/STM32H7xx_HAL_Driver/Inc/*",
        "Drivers/CMSIS/Include/*",
        "Drivers/CMSIS/Device/ST/STM32H7xx/Include/*",
        "Drivers/CMSIS/DSP/Include/*",
        "Drivers/CMSIS/DSP/Lib/GCC/*",
    )

    def package(self):
        copy(self, "*",
             src=os.path.join(self.source_folder, "Drivers"),
             dst=os.path.join(self.package_folder, "Drivers"))

    def package_info(self):
        self.cpp_info.includedirs = [
            "Drivers/STM32H7xx_HAL_Driver/Inc",
            "Drivers/STM32H7xx_HAL_Driver/Inc/Legacy",
            "Drivers/CMSIS/Include",
            "Drivers/CMSIS/Device/ST/STM32H7xx/Include",
            "Drivers/CMSIS/DSP/Include",
        ]
        self.cpp_info.srcdirs = ["Drivers/STM32H7xx_HAL_Driver/Src"]
        self.cpp_info.libdirs = ["Drivers/CMSIS/DSP/Lib/GCC"]
        self.cpp_info.libs = ["arm_cortexM7lfdp_math"]
        self.cpp_info.defines = ["USE_HAL_DRIVER"]
