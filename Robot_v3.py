#!usr/bin/python

import time
import signal
import subprocess
import os
import sys
import tty, termios
from datetime import datetime
import RPi.GPIO as GPIO

## Sets GPIO to use GPIO (BCM) number or Pin (BOARD)
print" 1 > Setting GPIO to BCM"
time.sleep(2)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

# Variables
print" 2 > Setting variable delay"
time.sleep(2)
delay = 0.0025
steps = 100

# Enable GPIO pins for ENA and ENB 
print" 3 > Setting GPIO pins for motor INPUT"
time.sleep(2)
coil_A_1_pin = 17  #pin 11 L298 IN1
coil_A_2_pin = 13  #pin 33 L298 IN2
coil_B_1_pin = 27  #pin 13 L298 IN3
coil_B_2_pin = 18  #pin 12 L298 IN4

# Set GPIO pin states
print" 4 > Setting GPIO pin SETUP"
time.sleep(2)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

# STOP MOTORS 
print" 5 -> Setting ENA1_2 and ENB1_2 to = FALSE "
print"    >> reset to LOW = NO MOVEMENT"
time.sleep(2)
GPIO.output(coil_A_1_pin, False)
GPIO.output(coil_A_2_pin, False)
GPIO.output(coil_B_1_pin, False)
GPIO.output(coil_B_2_pin, False)
time.sleep(3)

### Identifies Key strokes entered
print" 6 -> Creating Command Options"
def getch():
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   return ch

while True:
   print"\nCOMMAND OPTIONS:\n> w =FORWARD\n> s =BACK\n> a =LEFT or d =RIGHT\n> q =ROTATE LEFT or e =ROTATE RIGHT\n -> 0 to Exit\n -> 1 =Picture\n -> 2 =Motion Detection\n -> 3 =Range Sensor\n  -----------------------------\n Enter Command =  "

   char = getch()
   if(char == "1"):
      t = datetime.now()
      timestamp = '%d:%d-%d-%d' % (t.hour, t.minute, t.day, t.year)
      print "TIME = ", timestamp
      print" *** Taking a Picture ***", timestamp
      c = subprocess.Popen('raspistill -o picture-%d:%d-%d-%d' % (t.hour, t.minute, t.day, t.year), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
      for line in c.stdout.readlines():
         print line, 
      retval = c.wait()
      print"> Picture Taken", timestamp

   if(char == "2"):
      SENSE = 4
      GPIO.setup(SENSE, GPIO.IN)
      print"\n-> Setting Motion Sensor GPIO to = ", SENSE
      while 1:
         if GPIO.input(SENSE) == GPIO.LOW:
            print" -> Sensor Triggered -> MOTION ALERT", GPIO.input
            time.sleep(1) 
         else:
            print"-> Checking for Movement", GPIO.input
            time.sleep(.5)
   if(char == "w"):
      print"MOVING FORWARD"
      GPIO.output(coil_A_1_pin, False)
      GPIO.output(coil_A_2_pin, True)  #Right Track Motor Forward
      GPIO.output(coil_B_1_pin, False)
      GPIO.output(coil_B_2_pin, True)  #Left Track Motor Forward
      time.sleep(0.5)
      GPIO.output(coil_A_1_pin, False)
      GPIO.output(coil_A_2_pin, False)
      GPIO.output(coil_B_1_pin, False)
      GPIO.output(coil_B_2_pin, False)
   if(char == "s"):
      print"MOVING BACKWORDS"
      GPIO.output(coil_A_1_pin, True)  #Left Track Motor Backward
      GPIO.output(coil_A_2_pin, False)
      GPIO.output(coil_B_1_pin, True)  #Right Track Motor Backward 
      GPIO.output(coil_B_2_pin, False)
      time.sleep(0.5)
      GPIO.output(coil_A_1_pin, False)
      GPIO.output(coil_A_2_pin, False)
      GPIO.output(coil_B_1_pin, False)
      GPIO.output(coil_B_2_pin, False) 
   if (char == "a"):
      print"MOVING LEFT"
      GPIO.output(coil_A_1_pin, False)
      GPIO.output(coil_A_2_pin, True)    #Right Track Motor Forward
      GPIO.output(coil_B_1_pin, False)
      GPIO.output(coil_B_2_pin, False)
      time.sleep(0.1)
      GPIO.output(coil_A_1_pin, False)
      GPIO.output(coil_A_2_pin, False)
      GPIO.output(coil_B_1_pin, False)
      GPIO.output(coil_B_2_pin, False)  
   if (char == "q"):
      print"ROTATING LEFT"
      GPIO.output(coil_A_1_pin, False)
      GPIO.output(coil_A_2_pin, True)  #Right Track Motor Forward
      GPIO.output(coil_B_1_pin, True)  #Left Track Motor Backward
      GPIO.output(coil_B_2_pin, False)
      time.sleep(0.1)
      GPIO.output(coil_A_1_pin, False)
      GPIO.output(coil_A_2_pin, False)
      GPIO.output(coil_B_1_pin, False)
      GPIO.output(coil_B_2_pin, False)
   if (char == "d"):
      print"MOVING RIGHT"
      GPIO.output(coil_A_1_pin, False)
      GPIO.output(coil_A_2_pin, False)
      GPIO.output(coil_B_1_pin, False)
      GPIO.output(coil_B_2_pin, True)  #Left Track Motor Forward 
      time.sleep(0.1)
      GPIO.output(coil_A_1_pin, False)
      GPIO.output(coil_A_2_pin, False)
      GPIO.output(coil_B_1_pin, False)
      GPIO.output(coil_B_2_pin, False)
   if (char == "e"):
      print"ROTATING RIGHT"
      GPIO.output(coil_A_1_pin, True)  #Right Track Motor Backward
      GPIO.output(coil_A_2_pin, False)
      GPIO.output(coil_B_1_pin, False)
      GPIO.output(coil_B_2_pin, True)  #Left Track Motor Forward
      time.sleep(0.1)
      GPIO.output(coil_A_1_pin, False)
      GPIO.output(coil_A_2_pin, False)
      GPIO.output(coil_B_1_pin, False)
      GPIO.output(coil_B_2_pin, False)
   if (char == "x"):
      print"STOPPING"
      GPIO.output(coil_A_1_pin, False)
      GPIO.output(coil_A_2_pin, False)
      GPIO.output(coil_B_1_pin, False)
      GPIO.output(coil_B_2_pin, False)
   if (char =="z"):
      print"HARD STOP"
      GPIO.output(coil_A_1_pin, False)
      GPIO.output(coil_A_2_pin, True)
      GPIO.output(coil_B_1_pin, False)
      GPIO.output(coil_B_2_pin, True)


   if(char == "0"):
      raise SystemExit

raise SystemExit



# Motor Driver
print" 7 -> Setting sequence based on number of Steps"

def setStep(w1, w2, w3, w4):
   GPIO.output(coil_A_1_pin, w1)
   GPIO.output(coil_A_2_pin, w2)
   GPIO.output(coil_B_1_pin, w3)
   GPIO.output(coil_B_2_pin, w4)

print"   >>> w1234 set"
i = 0
print"   >> First Step Range i = ", i
for i in range(0, steps):
   setStep(1,0,1,0)
   time.sleep(delay)
   setStep(0,1,1,0)
   time.sleep(delay)
   setStep(0,1,0,1)
   time.sleep(delay)
   setStep(1,0,0,1)
   time.sleep(delay)
   print" Steps = ", steps
   time.sleep(1)

print"   >> Second Step Range i = ", i
for i in range(0, steps):
   setStep(1,0,0,1)
   time.sleep(delay)
   setStep(0,1,0,1)
   time.sleep(delay)
   setStep(0,1,1,0)
   time.sleep(delay)
   setStep(1,0,1,0)
   time.sleep(delay)
   print" Steps = ", steps
   time.sleep(1)

print"CLEAN UP GPIO"
GPIO.cleanup()
time.sleep(5)
print">> reset ENA & ENB to LOW"
time.sleep(2)
#GPIO.output(enable_a, False)
#GPIO.output(enable_b, False)


print" ---> EXITING <---"
raise SystemExit
