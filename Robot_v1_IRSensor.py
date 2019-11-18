#!usr/bin/python

import time
import signal
import subprocess
import os
import sys
import RPi.GPIO as GPIO


## Sets GPIO to use GPIO (BCM) number or Pin (BOARD)
print"\nSetting GPIO to BCM\n"
time.sleep(2)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO.cleanup()


### NEEDS TO BE REF OR FUNCTION CALL
## Getting Current Time
from datetime import datetime
t = datetime.now()
timestamp = '%d:%d-%d-%d' % (t.hour, t.minute, t.day, t.year)
print "\n\n\n   Info: TimeStamp = ", timestamp

## specific to motion sensor
SENSE = 4  # which is pin 7 as input pin for motion detection

print"\nDEBUG -> Sensor = ", SENSE
GPIO.setup(SENSE, GPIO.IN)
print"\n-> Setting Motion Sensor GPIO to = ", SENSE
#####

### NEEDS TO BE REF OR FUNCTION CALL
##Motion sensor takes picture 
while 1:
   if GPIO.input(SENSE) == GPIO.LOW:
      print"-> Sensor Triggered MOTION ALERT ALERT", GPIO.input
      time.sleep(1)
## play joker sound
#      p = subprocess.Popen('omxplayer /home/pi/joker_laugh.mp3', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#      for line in p.stdout.readlines():
#         print line, 
#      retval = p.wait()
## end sound

## take a picture:w

      t = datetime.now()
      timestamp = '%d:%d-%d-%d' % (t.hour, t.minute, t.day, t.year)
      print "TIME = ", timestamp
      print"----- Taking a Picture ", timestamp
      c = subprocess.Popen('raspistill -o Picture-%d:%d-%d-%d' % (t.hour, t.minute, t.day, t.year), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
      for line in c.stdout.readlines():
         print line, 
      retval = c.wait()
      print"> Picture Taken", timestamp  
   else:
      print" Checking for Movement  ", GPIO.input 
      time.sleep(.5)

## use omxplayer hello_monster.mp3
exit 

#      p = subprocess.Popen(["omcplayer /home/pi/joker_laugh.mp3"])
#      Camera = raspistill -o <file name>
#      Video  = raspivid -o vid.h264
#         - raspivid -o video.h264 -t 10000   ## will record for 10 seconds
