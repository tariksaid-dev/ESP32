try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

import ntptime
import utime
#actualizar el reloj interno mediante librería. Un poco pocho, marca 1 hora menos.
#para hacer esto correctamente hay que machine.RTC().datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))
#cortando la api a la que hago la call mejor. Actualizar cada vez que se conecte internet 1 sola vez.
#también podría usar este valor para mostrar en la web, en vez de la api mostramos el RTC de la placa. Así
#siempre sabrás que hora maneja la placa y no habrá erroes posible. Existe la casuística de que el tiempo cambie y tu tengas
#X horas seleccionadas. Qué hacer en ese caso?
def actualizar_reloj_interno():
    ntptime.host = "hora.roa.es"
    ntptime.settime()
    print(f"Hora actual: {utime.localtime()}")

credentials_txt = []

with open('credentials.txt', 'r') as credentials:
  linea = credentials.readline()
  while linea:
     credentials_txt.append(linea.strip())
     linea = credentials.readline()

ssid = credentials_txt[0]
password = credentials_txt[1]

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print(f'Conectado correctamente a la red {ssid}')
actualizar_reloj_interno()
print(station.ifconfig())
