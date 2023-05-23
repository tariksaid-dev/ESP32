from BLE import BLEUART
import utime
import ubluetooth as bluetooth
import gc
import usocket as socket
import network
import esp
esp.osdebug(None)
gc.enable()

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


station = network.WLAN(network.STA_IF)
station.active(True)

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
        while not station.isconnected() and utime.time() - \
                tiempo_inicial < MAX_CONEXION_WIFI:
            utime.sleep_ms(1000)
        if station.isconnected():
            pass
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

print(f'Conectado correctamente a la red {ssid}')
print(station.ifconfig())
