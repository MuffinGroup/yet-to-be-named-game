from cx_Freeze import setup, Executable
import os

# Define the list of files and folders to include
include_files = [
    'src/main/common/registries/alerts.py',
    'src/main/common/registries/animations.py',
    'src/main/common/registries/colors.py',
    'src/main/common/registries/elements.py',
    'src/main/common/registries/gui.py',
    'src/main/common/registries/items.py',
    'src/main/common/registries/language.py',
    # Include a directory and its contents
    ("src", "main")
]

setup(
    name="YourProgram",
    version="0.1",
    description="Description of your program",
    executables=[Executable("src/main/common/main.py")],
    options={
        "build_exe": {
            "include_files": include_files
        }
    }
)
