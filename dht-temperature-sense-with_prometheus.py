# RUN THIS FILE FROM THE VIRTUAL ENVIRONMENT UNDER /home/medha/sensor-project
# SOURCE /home/medha/sensor-project/bin/activate to ACTIVATE THE VENV. JUST RUN deactivate to exit the venv


# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_dht

# Import Prometheus Python Client
# Pre-requisite: Installed on Pi host: pip install prometheus-client
# Reference: https://pypi.org/project/prometheus-client/
from prometheus_client import Gauge
from prometheus_client import start_http_server

# Create Gauge metric objects for LPG, Methane and Smoke
rvce_temp_centigrade_gauge = Gauge("rvce_temp_centigrade", "Temp(C)")
rvce_temp_fahrenheit_gauge = Gauge("rvce_temp_fahrenheit", "Temperature(F)")
rvce_humidity_gauge = Gauge("rvce_humidity", "Humidity(%)")

# Start up the HTTP server to expose the metrics.
start_http_server(8000);

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D6)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity

        rvce_temp_centigrade_gauge.set(temperature_c)
        rvce_temp_fahrenheit_gauge.set(temperature_f)
        rvce_humidity_gauge.set(humidity)
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)
