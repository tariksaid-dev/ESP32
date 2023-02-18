try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)
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
print(station.ifconfig())

#led = Pin(2, Pin.OUT)

import gc
gc.collect()


ssid = 'DIGIFIBRA-sZu6'
password = 'UybNPKTy5Z'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print(f'Conectado correctamente a la red {ssid}')
print(station.ifconfig())

#led = Pin(2, Pin.OUT)
