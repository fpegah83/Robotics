#!/usr/bin/python

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)  #use board pin numbers
# define pin 7 as input pin
pin = 7
GPIO.setup(pin, GPIO.IN)

while 1:
   if GPIO.input(pin) == GPIO.LOW:
      print"-> Sensor Triggered ALERT ALERT", GPIO.input
      time.sleep(3)
   else:
      print" Checking for Movement  ", GPIO.input 
      time.sleep(.5)


exit 

