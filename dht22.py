import Adafruit_DHT
import time

 

sensor = Adafruit_DHT.DHT22
gpio = 4
 
print("'STRG + C' drücken, um Script zubeenden")
try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
 
        if humidity is not None and temperature is not None:
            print('Temperatur={0:0.1f}*  Luftfeuchtigkeit={1:0.1f}%'.format(temperature, humidity))
        else:
            print('Fehler, versuchs nochmal!')
        time.sleep(2)
except KeyboardInterrupt:
    print("Script wurde beendet")