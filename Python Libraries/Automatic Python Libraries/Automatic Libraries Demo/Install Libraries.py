import subprocess
import sys
import re
import os

# Path to the script that needs library installation
script_path = "your_script.py"
# Path to your .bat file
bat_file = "install_libraries.bat"

# Read the script file and detect library imports
with open(script_path, "r") as f:
    content = f.read()
    libraries = set(re.findall(r'^\s*(?:import|from)\s+(\w+)', content, re.MULTILINE))

# List to store missing libraries
missing_libraries = []

# Check each library
for lib in libraries:
    try:
        __import__(lib)
        print(f"{lib} is already installed.")
    except ImportError:
        print(f"{lib} is missing.")
        missing_libraries.append(lib)

# If there are missing libraries, call the .bat file
if missing_libraries:
    print("Installing missing libraries...")
    # Call the .bat file with the missing libraries as arguments
    subprocess.call([bat_file] + missing_libraries)
else:
    print("All libraries are already installed.")
