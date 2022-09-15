# Raspberry Pi Detector
# By @bupboi1337
# Note: This program is licenced under the GPL V3 licence, see LICENCE to see the licence.
# Editors can put thier here:
#

import os
print("Raspberry Pi Detector")
print("This uses the GPL V3 Licence. Read the file LICENCE to see it.")
a = "raspberrypi.local" # Name of the default Raspberry Pi LAN Hostname
b = os.system("ping -c 1 " + a) # Ping raspberrypi.local on the LAN network and save the results as a variable
print("Pinging local Raspberry Pi IP Address...")

# check the response
if b == 0: # if the ping variable is zero then the ping went through correctly
    print('RPi local address ping successful! There is a Raspberry Pi on your Network!')
else: # If the ping variable is anything but zero then it will show this error
    print('RPi local address ping failed! There is probably not a Raspberry Pi on your network.')
