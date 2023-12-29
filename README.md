# birthday_minder.py / .shl
#
# Birthday Minder V1.0 
# Raspberry PI with 1.3" TFT Adafruit display
# Author: J. Nolan (totorodad@gmail.com)
# 9-Sept-2023
# Release 1.0 (no restriction apply)
#
# Pre-requisits:
#	sudo apt-get update
# 	sudo apt-get install python3-pip
#	sudo pip update
#	sudo apt-get install python3-pil
#	sudo apt-get install ttf-dejavu
#	sudo pip install adafruit-circuitpython-rgb-display
#
# Copy this program to your /home/pi folder then
# Add this line to the last line of: /etc/xdg/lxsession/LXDE-pi/autostart
# @lxterminal --command "/home/pi/birthday_minder/birthday_minder.shl"
#
# Make sure to turn on I2C for the display with the
# raspberry pi configuration tool.
# It's also a good idea to turn on VNC and SSH after setting up a fresh
# PI.  Enable Wifi by logging into your local router.
#
# Revision History
# 9-Sept-2023: Modfied from read aqi
# 28-Sept-2023: Added number of days to next birthday
