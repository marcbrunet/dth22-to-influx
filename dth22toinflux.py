from influxdb import InfluxDBClient
import Adafruit_DHT
import socket
import time


DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

client = InfluxDBClient(host='192.168.0.101', port=8086, username='marc', password='marc')
client.create_database('sensors')
client.switch_database('sensors')
measurement = "rpi-dht22"
location = socket.gethostname()


while True:
    try:
        # Print the values to the serial port
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        print("Temp: {:.1f} C   Humidity: {}% ".format(temperature, humidity))
        iso = time.ctime()
        data = [
            {
                "measurement": measurement,
                "tags": {
                    "location": location,
                },
                "time": iso,
                "fields": {
                    "temperature": temperature,
                    "humidity": humidity
                }
            }
        ]
        client.write_points(data)

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
    time.sleep(60)
