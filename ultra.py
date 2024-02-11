from gpiozero import DistanceSensor
import time

#ultrasonic = DistanceSensor(echo=16, trigger=4)

#while True:
#    print(ultrasonic.distance *100)
#    time.sleep(5)

def start_motor():
    print("Starting...")

def stop_motor():
    print("Something is blocking ahead. Stopping...")

ultrasonic = DistanceSensor(echo=16, trigger=4)
ultrasonic.threshold_distance = 0.5
ultrasonic.when_in_range = stop_motor
ultrasonic.when_out_of_range = start_motor

while True:
  print("Sleeping...")
  time.sleep(5)
