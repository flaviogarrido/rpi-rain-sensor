import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#define the pin that goes to the circuit
pin_D0 = 16
pin_A0 = 20

#setup
GPIO.setup(pin_D0, GPIO.IN)

def rc_time (pin_to_circuit):
    count = 0
    return

    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)

    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interupted, cleanup correctly
try:
    # Main loop
    while True:
        value_A0 = rc_time(pin_A0)
	value_D0 = GPIO.input(pin_D0)
        #print "D0 = %s e A0 = %s" % (value_D0, value_A0)
	if value_D0:
		print "Tempo seco"
	else:
		print "Chuva"

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()


