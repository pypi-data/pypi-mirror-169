"""
:authors: Superior_6564
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2022 Superior_6564
"""
import time
import subprocess
import sys


def install():
    """
    Args:

    """
    """
    Description:
        required() installs required packages .
    """
    def install_package(package: str, output: bool = True, version: str = None):
        print(f"Start installing package named {package}")
        try:
            new_package = package + "==" + version
            subprocess.check_call([sys.executable, "-m", "pip", "install", new_package])
            if output:
                print(f"Library {package}({version}) installed.")
        except subprocess.CalledProcessError:
            print(f"ERROR with {package}.")
            print("ERROR: Bad name or Bad version.")

    require = ["requests", "ipython", "dearpygui"]
    versions = ["2.28.1", "7.34.0", "1.7.1"]
    print("Installing the required libraries...")
    for i in range(len(require)):
        install_package(package=require[i], version=versions[i])
        print(f"Status: {i + 1} of {len(require)}")
        time.sleep(2)
    print("Installation is complete.")
