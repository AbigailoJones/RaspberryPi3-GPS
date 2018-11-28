# Basic Python Functions for GPS/RPi

#Imports

import GPS
import threading
import time

class GPS_init(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global gpsd
        gpsd = gps(mode=WATCH_ENABLE)
        self.current_value = None
        self.running = True
    def run(self):
        global gpsd
        while gpsp.running:
            gpsd.next() 

class GPS_get:
    def GetCoords(self):
        gpsd.next()
        latlon = gpsd.fix.latitude, gpsd.fix.longitude
        while latlon == (0.0, 0.0):
        	time.sleep(.5)
        	gpsd.next()
        	latlon = gpsd.fix.latitude, gpsd.fix.longitude
        return latlon



