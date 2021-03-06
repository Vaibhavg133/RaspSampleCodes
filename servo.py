'''
Use this simple code to interface your servo with the Raspberry Pi 3
Connect Signal wire to the 11 pin GPIO17
'''
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
p=GPIO.PWM(11,50)
sleeptime=3
p.start(7.5)
try:
	while True:
		p.ChangeDutyCycle(7.5) #Neutral
		time.sleep(sleeptime)
		print "0"
		p.ChangeDutyCycle(12.5) #180
		time.sleep(sleeptime)
		print "180"
		p.ChangeDutyCycle(2.5) #0
		time.sleep(sleeptime)
		print "90"
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
