import utime
import ntptime
import ubluetooth as bluetooth
import gc
from BLE import BLEUART
try:
    import usocket as socket
except:
    import socket
import network
import esp
esp.osdebug(None)
gc.collect()

# actualizar el reloj interno mediante librería. Un poco pocho, marca 1 hora menos.
# para hacer esto correctamente hay que machine.RTC().datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))
# cortando la api a la que hago la call mejor. Actualizar cada vez que se conecte internet 1 sola vez.
# también podría usar este valor para mostrar en la web, en vez de la api mostramos el RTC de la placa. Así
# siempre sabrás que hora maneja la placa y no habrá erroes posible. Existe la casuística de que el tiempo cambie y tu tengas
# X horas seleccionadas. Qué hacer en ese caso?


def actualizar_reloj_interno():
    ntptime.host = "hora.roa.es"
    ntptime.settime()
    print(f"Hora actual: {utime.localtime()}")


archivo = "credentials.txt"
MAX_CONEXION_WIFI = 15


def leer_credenciales():
    try:
        with open(archivo, "r") as f:
            ssid = f.readline().strip()
            password = f.readline().strip()
        if ssid and password:
            return ssid, password
        else:
            return None, None
    except FileNotFoundError:
        return None, None


def escribir_credenciales(ssid=None, password=None):
    if ssid and password:
        with open(archivo, "w") as f:
            f.write(ssid + "\n")
            f.write(password + "\n")


def borrar_credenciales():
    with open(archivo, "w") as f:
        f.write("")


def on_rx():
    rx_buffer = uart.read().decode().strip()
    data.append(rx_buffer)
    print(rx_buffer)


# Init modo estación
station = network.WLAN(network.STA_IF)
station.active(True)

# todo: bucle infinito en la segunda vuelta si detecta dos
# líneas en el archivo credentials.
while not station.isconnected():
    data = []
    ssid, password = leer_credenciales()
    if ssid and password:
        print("Conectando a la red wifi...")
        print(ssid)  # traza
        print(password)  # traza
        station.disconnect()
        station.connect(ssid, password)
        tiempo_inicial = utime.time()
        while not station.isconnected() and utime.time() - tiempo_inicial < MAX_CONEXION_WIFI:
            utime.sleep_ms(1000)
        if station.isconnected():
            print(f'Conectado correctamente a la red {ssid}')
        else:
            borrar_credenciales()
            print("No se pudo conectar a la red Wi-Fi. Cambiando a modo BLE...")
            ble = bluetooth.BLE()
            uart = BLEUART(ble, "ESP32")
            while len(data) < 2:
                uart.irq(handler=on_rx)
                utime.sleep_ms(1000)
                if len(data) == 2:
                    escribir_credenciales(data[0], data[1])
                    print("Credenciales recibidas por Bluetooth")
                    uart.close()
    else:
        borrar_credenciales()
        print("No se encuentra la SSID/Password. Cambiando a modo Ble...")
        ble = bluetooth.BLE()
        uart = BLEUART(ble, "ESP32")
        while len(data) < 2:
            uart.irq(handler=on_rx)
            utime.sleep_ms(1000)
            if len(data) == 2:
                escribir_credenciales(data[0], data[1])
        print("Credenciales recibidas por Bluetooth")
        uart.close()
    # podría hacer un elif con un código para hacer bypass al bucle
    # por si fuera imprescindible un arranque sin conexión.

print(f'Conectado correctamente a la red {ssid}')
# actualizar_reloj_interno()
print(station.ifconfig())
