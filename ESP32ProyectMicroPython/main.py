import ujson as json
import urequests as requests
import time

def make_request(url):
    print("Cargando los datos...")
    response = requests.get(url)
    if(response.status_code == 200):
        print("Datos cargados con éxito")
        data = response.json()
        for hora in data.values():
            hours.append(hora["hour"])
            prices.append(hora["price"])
    else:
        print("Error, no se pudieron cargar los datos")
        
def get_hora(url):
    print("Obteniendo la hora de Madrid, España")
    response = requests.get(url)
    if(response.status_code == 200):
        print("Hora cargada con éxito")
        data = response.json()
        return data['datetime']
    else:
        print("Error en la API, no se pudo obtener la hora")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

# Api de semi/pago, cambiar en producto final o pagar 9$ mes para uso ilimitado
URL_API_HORA = "https://timezone.abstractapi.com/v1/current_time/?api_key=1efba11478714b6599e5d95b2b0762f1&location=Madrid,%Spain"
URL_API_LUZ = "https://api.preciodelaluz.org/v1/prices/all?zone=PCB"
INTERVALO = 60000

hora_ultima_actualizacion = ""
hours = []
prices = []
ultima_actualizacion = time.ticks_ms()



while True:
    if time.ticks_diff(time.ticks_ms(), ultima_actualizacion) >= INTERVALO:
        make_request(URL_API_LUZ)
        ultima_actualizacion = time.ticks_ms()
        hora_ultima_actualizacion = get_hora(URL_API_HORA)
        print(hora_ultima_actualizacion)

