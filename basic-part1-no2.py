#Write a Python program to get the Python version you are using
# Solution 1
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

# Solution 2
import platform
print(platform.python_version())