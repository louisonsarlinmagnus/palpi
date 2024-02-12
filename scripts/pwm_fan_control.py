import RPi.GPIO as GPIO
import time
import subprocess

GPIO_PIN = 14

GPIO.setmode(GPIO.BCM)
##Set to false, other processes occupying the pin will be ignored
GPIO.setwarnings(False)
GPIO.setup(GPIO_PIN, GPIO.OUT)
pwm = GPIO.PWM(GPIO_PIN,100)

dc = 0
pwm.start(dc)

try:
    while True:
        temp = float(subprocess.getoutput("vcgencmd measure_temp|sed 's/[^0-9.]//g'"))
        time.sleep(1)
        if temp >= 80:
            dc = 100
            pwm.ChangeDutyCycle(dc)
        else:
            dc = 0
            pwm.ChangeDutyCycle(dc)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()