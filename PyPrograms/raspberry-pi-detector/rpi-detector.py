# Raspberry Pi Detector
# By @bupboi1337
# editor names go here:
#

import os
hostname = "raspberrypi.local" # Raspberry Pi Local Hostname
response = os.system("ping -c 1 " + hostname) # Ping raspberrypi.local

# check the response
if response == 0: # If the ping went through correctly
  print hostname, 'detected! There is a Raspberry Pi on your Network!'
else: # If the ping was unsuccessful
  print hostname, 'not found! There is probably not a Raspberry Pi on your network.'
