# System Informaiton
# By @bupboi1337
# This uses the GPL V3 licence btw

import platform # import the Platform module to be able to scan the users system

print("="*40, "System Information by @bupboi1337", "="*40)
uname = platform.uname()
print(f"System: {uname.system}") 
print(f"Release: {uname.release}") 
print(f"Version: {uname.version}") 
print(f"Machine: {uname.machine}") 
