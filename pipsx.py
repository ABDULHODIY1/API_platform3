import os
import subprocess

print("Library Name?")
Lib = input("[:]")

os.system(f"python3 -m pip install {Lib}")

installed_libs = subprocess.run(["pip", "freeze"], capture_output=True, text=True)

with open("requirements.txt", "w") as f:
    f.write(installed_libs.stdout[9:-1])

print("Task is Successful")
