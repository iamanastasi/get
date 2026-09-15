import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led = 26
delitel = 6
GPIO.setup(led, GPIO.OUT)
GPIO.setup(delitel, GPIO.IN)
state = 0
while True:
    if(GPIO.input(delitel)):
        state=0
    else:
        state=1
    GPIO.output(led, state)