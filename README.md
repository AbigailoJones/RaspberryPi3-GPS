# RaspberryPi3-GPS
Care and feeding of MTK3339 chipset via UART, using gpsd, on the RPI3, and Raspbian Jessie or later. (and Python)
Mashed together from Adafruit tutorial 

https://learn.adafruit.com/adafruit-ultimate-gps-on-the-raspberry-pi/introduction

And general noodling around

# Wire it up

GPS vin to RPI3 3.3v

GPS ground to RPI3 ground

GPS rx to RPI3 tx

GPS tx to RPI3 rx

# Configurating to use Serial Port

sudo raspi-config

select 5- interfacing options

select P6- serial

NO for login shell

YES for serial port hardware

reboot

#####
# Downloads and Fixes
#####

Get GPSD

sudo apt-get install gpsd gpsd-clients

Fix systemd socket error in Jessie and later

sudo systemctl stop gpsd.socket

sudo systemctl disable gpsd.socket

Point gpsd to TTYS0  

sudo killall gpsd

sudo gpsd /dev/ttyS0 -F /var/run/gpsd.sock

# Check for Data 
(sometimes pointing it out the window or setting it on a porch with the antenna facing the sky is necessary)

check for data with

cgps -s


# Have Data? Good.
(Don't have data? Hold on, we'll get there someday)

