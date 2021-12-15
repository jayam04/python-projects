# Raspberry Pi Detector
# By @bupboi1337
# Note: This program is licenced under the GPL V3 licence, see LICENCE to see the licence.
# Editor names go here:
#

import os
print("Raspberry Pi Detector")
print("This uses the GPL V3 Licence. Read the file LICENCE to see it.")
ip = "raspberrypi.local" # Name of the default Raspberry Pi Local Hostname
ping = os.system("ping -c 1 " + a) # Ping raspberrypi.local
print("Pinging local Raspberry Pi IP Address...")

# check the response
if ping == 0: # If the ping worked
  print('RPi local address ping successful! There is a Raspberry Pi on your Network!')
else: # If the ping failed
  print('RPi local address ping failed! There is probably not a Raspberry Pi on your network.')
