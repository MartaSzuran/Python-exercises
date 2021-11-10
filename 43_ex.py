# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to get OS name, platform and release information.
# # Exercise 43

# os.name: The name of the operating system dependent module imported.
# The following names have currently been registered: 'posix', 'nt', 'java'.
# platform.system(): Return the name of the OS system is running on.
# platform.release(): Return the version of the operating system.

# first solution
import platform
import os

print("Name of the operating system:", os.name)
print("\nName of the OS system:", platform.system())
print("\nVersion of the operating system:", platform.release())


# second solution
import os
import sys
import platform
import sysconfig
print("os.name                     ", os.name)
print("sys.platform                ", sys.platform)
print("platform.system()           ", platform.system())
print("sysconfig.get_platform()    ", sysconfig.get_platform())
print("platform.machine()          ", platform.machine())
print("platform.architecture()     ", platform.architecture())
