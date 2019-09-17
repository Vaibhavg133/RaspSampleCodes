import RPi.GPIO as GPIO
import time
def distancerun():
	GPIO.output(Trig,False)
	time.sleep(0.1)
	GPIO.output(Trig,True)
	time.sleep(0.00001)
	GPIO.output(Trig,False)
	while GPIO.input(Echo)==0:
		pass
	start=time.time()
	while GPIO.input(Echo)==1:
		pass
	stop=time.time()
	distance=(stop-start)*17000
	return distance
Trig=7
Echo=12
servo=11
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Trig,GPIO.OUT)
GPIO.setup(Echo,GPIO.IN)
GPIO.setup(servo,GPIO.OUT)
p=GPIO.PWM(servo,50)
sleeptime=2
p.start(7.5)
try:
	while True:
		p.ChangeDutyCycle(7.5)
		#time.sleep(5)
		zero=distancerun()
		print "zero : ",zero
		time.sleep(sleeptime)

		p.ChangeDutyCycle(12.5)
		#time.sleep(5)
		oneeighty=distancerun()
		print "one-eighty : ",oneeighty
		time.sleep(sleeptime)

		p.ChangeDutyCycle(2.5)
		#time.sleep(5)
		ninty=distancerun()
		print "ninty : ",ninty
		time.sleep(sleeptime)
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
