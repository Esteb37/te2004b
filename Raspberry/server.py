import Adafruit_DHT
import sys
import Adafruit_DHT

DHT_SENSOR = adafruit_DHT.DHT11
DHT_PIN = 4

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysock.bind(("", 32003))

except:
    print("Failed to bind")
    sys.exit()

mysock.listen(5)
conn, addr = mysock.accet()
print("connection from: " + str(addr))

while True:
    data = conn.rev(1024).decode()
    if not data:
        print("Shutdown Server")
        break

    hum, temp = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if hum is not None and temp is not None:
        tempHum = str("Temp=(0:0.1f)C Humidity=(0:0.1f)%").format(temp, hum)
        print(tempHum)
