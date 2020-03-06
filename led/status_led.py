import RPi.GPIO as GPIO
from settings.parseSettings import get_Settings
Status_LED_Settings = get_Settings('STATUS_LED')


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(int(Status_LED_Settings['POWER']), GPIO.OUT)

def status_LED_ON():
	GPIO.output(int(Status_LED_Settings['POWER']), GPIO.HIGH)
	return
	
def status_LED_OFF():
	GPIO.output(int(Status_LED_Settings['POWER']), GPIO.LOW)
	return