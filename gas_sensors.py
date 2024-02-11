import RPi.GPIO as GPIO
import time

# Set up GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)  # Use the board pin number corresponding to GPIO 4
GPIO.setup(10, GPIO.IN)
GPIO.setup(12, GPIO.IN)
try:
    while True:
        # Read digital input from GPIO 4
        sensor_output_2 = GPIO.input(8)  # Use the board pin number
        sensor_output_137 = GPIO.input(10)
        sensor_output_136 = GPIO.input(12)
        # Print the result
        if sensor_output_2 == 0:
        	print("LPG detected")
        else:
                print("LPG absent")
        if sensor_output_137 == 0:
                print("Ammonia detected")
        else:
                print("Ammonia absent")
        if sensor_output_136 == 0:
                print("H2S detected")
        else:
                print("H2S absent")
        # Wait for a short duration before reading again
        print("----------------------------")
        time.sleep(1.5)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Clean up GPIO on program exit
    GPIO.cleanup()

