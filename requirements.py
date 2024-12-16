import subprocess
import sys
import os

def install_requirements():
    """Install all required packages"""
    requirements = [
        "customtkinter==5.2.2",
        "pillow==10.2.0",
        "ttkthemes==3.2.2",
        "numpy==1.24.3",
        "matplotlib==3.7.2"
    ]
    
    print("Installing required packages...")
    
    for package in requirements:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError as e:
            print(f"Error installing {package}: {e}")
            return False
    
    print("\nAll packages installed successfully!")
    return True

if __name__ == "__main__":
    if install_requirements():
        print("\nSetup complete! You can now run MindfulShift 2025.")
        input("Press Enter to exit...")