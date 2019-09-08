import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG=23
ECHO=24
print "Distance Measurement in Progress" 

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG,False)
print "Waiting for settle"
time.sleep(2)
GPIO.output(TRIG,True)
time.sleep(0.00001)
while True:
	while GPIO.input(ECHO)==0:
		pass	
	start=time.time()
	while GPIO.input(ECHO)==1:
		pass
	end=time.time()
	duration=end-start
	distance = duration * 17150
	distance = round(distance,2)
	print "Distance: ",distance,"cm"
GPIO.cleanup()
