# Raspberry Pi Detector
# By @bupboi1337
# Note: This program is licenced under GPL V3.
# editor names go here:
#

import os
print("Raspberry Pi Detector")
print("This uses the GPL V3 Licence. Read the file LICENCE to see it.")
a = "raspberrypi.local" # name of the Raspberry Pi Local Hostname
b = os.system("ping -c 1 " + a) # Ping raspberrypi.local
print("Pinging local Raspberry Pi IP Address...")

# check the response
if b == 0: # If the ping succedded
  print a, 'was pinged successfuly! There is a Raspberry Pi on your Network!'
else: # If the ping failed
  print a, 'was unable to be pinged! There is probably not a Raspberry Pi on your network.'
