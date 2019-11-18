#!usr/bin/python

import time
import RPi.GPIO as GPIO
import signal
import subprocess
import os
from datetime import datetime

t = datetime.now()
timestamp = '%d:%d-%d-%d' % (t.hour, t.minute, t.day, t.year)
print "TIME = ", timestamp

##GPIO Settings
GPIO.setmode(GPIO.BOARD)  #use board pin numbers
# define pin 7 as input pin
pin = 7
GPIO.setup(pin, GPIO.IN)

while 1:
   if GPIO.input(pin) == GPIO.LOW:
      print"-> Sensor Triggered ALERT ALERT", GPIO.input
      time.sleep(1)
      p = subprocess.Popen('omxplayer /home/pi/joker_laugh.mp3', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
      for line in p.stdout.readlines():
         print line,
      retval = p.wait()

      t = datetime.now()
      timestamp = '%d:%d-%d-%d' % (t.hour, t.minute, t.day, t.year)
      print "TIME = ", timestamp
      print"----- Taking a Picture ", timestamp
      c = subprocess.Popen('raspistill -o %d:%d-%d-%d' % (t.hour, t.minute, t.day, t.year), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
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
