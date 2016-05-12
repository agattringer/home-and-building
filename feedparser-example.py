USERNAME="xxx@gmail.com"
PASSWORD="xxxx"


import RPi.GPIO as GPIO
import feedparser
import time

while True:
	GPIO_PIN_NEW=18
	GPIO_PIN_READ=23
		
	GPIO.setwarnings(False)

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(GPIO_PIN_NEW, GPIO.OUT)
	GPIO.setup(GPIO_PIN_READ, GPIO.OUT)
	newmails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])
	
	if newmails > 0:
    		GPIO.output(GPIO_PIN_NEW, True)
		GPIO.output(GPIO_PIN_READ, False)
	else:
    		GPIO.output(GPIO_PIN_NEW, False)
		GPIO.output(GPIO_PIN_READ, True)
	
	print "sleeping"
	time.sleep(5)
	
