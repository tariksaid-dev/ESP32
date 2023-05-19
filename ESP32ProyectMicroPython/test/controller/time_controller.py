# import urequests as requests
import requests


class TimeController:
    def __init__(self):
        # 2023-05-18 14:03:03
        self.fecha_completa = ""

        # 14:03
        self.hora_string = ""

        # 14-15
        self.hora_intervalo = ""

    def set_hora(self):
        return self.get_fecha_completa_req()

    def get_fecha_completa(self):
        return self.fecha_completa

    def get_fecha_completa_req(self):
        print("Obteniendo la hora de Madrid, España")
        try:
            response = requests.get("https://timezone.abstractapi.com/v1/current_time/?api_key=1efba11478714b6599e5d95b2b0762f1&location=Madrid,%Spain")
            if (response.status_code == 200):
                data = response.json()
                print("Hora cargada con éxito")
                return data['datetime']
            else:
                print("Error en la API, no se pudo obtener la hora")
        except:
            return "Error al cargar la hora"

    def hora_mm_ss(self):
        try:
            return self.fecha_completa[11:16]
        except:
            return "??"
    
    def set_hora_intervalo(self):
        try:
            hora_actual = self.hora_string[0:2]
            hora_siguiente = str(int(hora_actual) + 1)
            if int(hora_actual) <= 9:
                return hora_actual + "-0" + hora_siguiente
            else:
                return hora_actual + "-" + hora_siguiente
        except:
            return "??"

    def cargar_hora(self):
        self.fecha_completa = self.set_hora()
        self.hora_string = self.hora_mm_ss()
        self.hora_intervalo = self.set_hora_intervalo()

    def __str__(self):
        return (f"""Fecha completa: {self.fecha_completa}\nHora: {self.hora_string}\nIntervalo actual: {self.hora_intervalo}
        """)

