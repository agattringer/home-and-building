import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

def on_connect(client, userdata, rc):
	print("connected with code " + str(rc))
	client.subscribe("lock_opener")

def on_message(client, userdata, msg):
	if msg.payload == "open":
		GPIO.output(18, True)
	elif msg.payload == "close":
		GPIO.output(18, False)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

client.connect("localhost", 1883, 60)
client.loop_forever()
