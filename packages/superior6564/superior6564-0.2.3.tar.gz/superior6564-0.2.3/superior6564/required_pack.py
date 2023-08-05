# from packages import install as install_package
from web import install_package
import time


def install():
    """
    Args:

    """
    """
    Description:
        required() installs required packages .
    """

    require = ["requests", "ipython", "dearpygui"]
    versions = ["2.28.1", "8.5.0", "1.7.1"]
    print("Installing the required libraries...")
    for i in range(len(require)):
        install_package(package=require[i], version=versions[i])
        print(f"Status: {i + 1} of {len(require)}")
        time.sleep(1)
    print("Installation is complete.")
