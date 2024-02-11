import RPi.GPIO as GPIO
from time import sleep
from gpiozero import DistanceSensor

in1 = 24
in2 = 23
en1 = 25  # Enable pin for motor 1
in3 = 17
in4 = 27
en2 = 22  # Enable pin for motor 2

temp1 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en1, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)

p1 = GPIO.PWM(en1, 1000)
p2 = GPIO.PWM(en2, 1000)

p1.start(25)
p2.start(25)

print("\n")
print("The default speed & direction of motors is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("1 - Low speed, 2 - Medium speed, 3 - High speed")
print("L - Left, R - Right")
print("\n")

def start_motor():
    print("Starting...")

def stop_motor():
    print("Something is blocking ahead. Stopping...")
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    x = 'z'
    is_blocked=1

ultrasonic = DistanceSensor(echo=16, trigger=4)
ultrasonic.threshold_distance = 0.5
ultrasonic.when_in_range = stop_motor
ultrasonic.when_out_of_range = start_motor

while True:

    x = input()

    if x == 'q':
        print("run")
        if temp1 == 1:
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            GPIO.output(in3, GPIO.HIGH)
            GPIO.output(in4, GPIO.LOW)
            print("forward")
            x = 'z'
        else:
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
            print("backward")
            x = 'z'

    elif x == 'e':
        print("stop")
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)
        x = 'z'

    elif x == 'w':
        print("forward")
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.HIGH)
        GPIO.output(in4, GPIO.LOW)
        temp1 = 1
        x = 'z'

    elif x == 's':
        print("backward")
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.HIGH)
        temp1 = 0
        x = 'z'

    elif x == '1':
        print("low")
        p1.ChangeDutyCycle(50)
        p2.ChangeDutyCycle(50)
        x = 'z'

    elif x == '2':
        print("medium")
        p1.ChangeDutyCycle(75)
        p2.ChangeDutyCycle(75)
        x = 'z'

    elif x == '3':
        print("high")
        p1.ChangeDutyCycle(100)
        p2.ChangeDutyCycle(100)
        x = 'z'

    elif x == 'a':
        print("left")
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in4, GPIO.HIGH)
        GPIO.output(in3, GPIO.LOW)
        x = 'z'
        sleep(0.5)
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)

    elif x == 'd':
        print("right")
        GPIO.output(in2, GPIO.HIGH)
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)
        GPIO.output(in3, GPIO.HIGH)
        x = 'z'
        sleep(0.5)
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)

    elif x == 'e':
        GPIO.cleanup()
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
