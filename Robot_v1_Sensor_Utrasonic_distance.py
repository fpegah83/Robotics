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


##############################
## specific to Distance ping and return sensor
TRIG = 23    #Trigger pin 16 
ECHO = 24    #Echo    pin 18 

## Distance measurement
print"Distance Measurement In Progress"
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
   pulse_start = time.time()

while GPIO.input(ECHO)==1:
   pulse_end = time.time()

pulse_duration = pulse_end - pulse_start
distance = pulse_duration * 17150
distance = round(distance, 2)

print "\nDistance:",distance,"cm"

# Convert centimeters to inches
CM_PER_INCH = 2.54   #cm in an inch
print"-> Converted to INCHES = ", (distance / CM_PER_INCH)

GPIO.cleanup()

##############################

print"\n*** EXITING SCRIPT ***"
raise SystemExit



### NEEDS TO BE REF OR FUNCTION CALL
## Getting Current Time
#from datetime import datetime
#t = datetime.now()
#timestamp = '%d:%d-%d-%d' % (t.hour, t.minute, t.day, t.year)
#print "\n\n\n   Info: TimeStamp = ", timestamp

## specific to motion sensor
#SENSE = 4  # which is pin 7 as input pin for motion detection

#print"\nDEBUG -> Sensor = ", SENSE
#GPIO.setup(SENSE, GPIO.IN)
#print"\n-> Setting Motion Sensor GPIO to = ", SENSE
#####

### NEEDS TO BE REF OR FUNCTION CALL
##Motion sensor takes picture 
while 1:
   if GPIO.input(pin7) == GPIO.LOW:
      print"-> Sensor Triggered MOTION ALERT ALERT", GPIO.input
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
