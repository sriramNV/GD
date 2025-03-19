import sys
from cx_Freeze import setup, Executable

# Specify the Python version to use
base = None
if sys.platform == "win64":
    base = "Win64GUI"  # This ensures the game runs without a console window (for GUI-based games)

# Specify the path to your main Python file
executables = [Executable("main.py", base=base)]

# Setup function for cx_Freeze
setup(
    name="My Game",
    version="1.0",
    description="A Pygame-based Game",
    executables=executables,
    options={
        'build_exe': {
            'include_files': [
                'resources',  # Include the resources folder and its contents
            ],
            'packages': ['pygame', 'collections', 'sys', 'functools', 'random'],  # Include Pygame if not automatically detected
        }
    }
)
