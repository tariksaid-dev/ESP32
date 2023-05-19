from time import sleep
import controller.time_controller as timecntrl
import controller.gpio_controller as gpiocntrl

# Datos cargados con éxito
# {'01-02': 87.96, '06-07': 101.63, '08-09': 129.74, '19-20': 140.55, '16-17': 65.34, '18-19': 127.02, '05-06': 101.46, '11-12': 133.14, '21-22': 200.29, '23-24': 133.84, '00-01': 98.33, '15-16': 71.11, '10-11': 140.01, '07-08': 120.68, '04-05': 100.84, '03-04': 88.33, '14-15': 70.63, '22-23': 149.56, '20-21': 173.02, '17-18': 71.58, '02-03': 86.84, '13-14': 118.58, '09-10': 103.82, '12-13': 127.3}
# --------------------------
# [('00-01', 98.33), ('01-02', 87.96), ('02-03', 86.84), ('03-04', 88.33), ('04-05', 100.84), ('05-06', 101.46), ('06-07', 101.63), ('07-08', 120.68), ('08-09', 129.74), ('09-10', 103.82), ('10-11', 140.01), ('11-12', 133.14), ('12-13', 127.3), ('13-14', 118.58), ('14-15', 70.63), ('15-16', 71.11), ('16-17', 65.34), ('17-18', 71.58), ('18-19', 127.02), ('19-20', 140.55), ('20-21', 173.02), ('21-22', 200.29), ('22-23', 149.56), ('23-24', 133.84)]
# --------------------------
# ['98.33', '87.96', '86.84', '88.33', '100.84', '101.46', '101.63', '120.68', '129.74', '103.82', '140.01', '133.14', '127.3', '118.58', '70.63', '71.11', '65.34', '71.58', '127.02', '140.55', '173.02', '200.29', '149.56', '133.84']
# Obteniendo la hora de Madrid, España
# Hora cargada con éxito
# 2023-05-18 21:23:38

datos_ordenados = [('00-01', 98.33), ('01-02', 87.96), ('02-03', 86.84), ('03-04', 88.33), ('04-05', 100.84), ('05-06', 101.46), ('06-07', 101.63), ('07-08', 120.68), ('08-09', 129.74), ('09-10', 103.82), ('10-11', 140.01), ('11-12', 133.14),
                   ('12-13', 127.3), ('13-14', 118.58), ('14-15', 70.63), ('15-16', 71.11), ('16-17', 65.34), ('17-18', 71.58), ('18-19', 127.02), ('19-20', 140.55), ('20-21', 173.02), ('21-22', 200.29), ('22-23', 149.56), ('23-24', 133.84)]

prices_str = ['98.33', '87.96', '86.84', '88.33', '100.84', '101.46', '101.63', '120.68', '129.74', '103.82', '140.01',
              '133.14', '127.3', '118.58', '70.63', '71.11', '65.34', '71.58', '127.02', '140.55', '173.02', '200.29', '149.56', '133.84']

hora = "2023-05-18 21:23:38"


def array_mas_baratos(array, valor):
    elementos = array
    elementos_ordenados = sorted([float(p) for p in elementos])
    elementos_baratos = elementos_ordenados[:int(valor)]
    elementos_baratos_str = [str(p) for p in elementos_baratos]
    return elementos_baratos_str


# Devuelve las horas más baratas recibiendo el array de tuplas y el valor (número de horas que deseamos)
def obtener_horas_mas_baratas(array, valor):
    # Ordenar por el segundo valor de la tupla
    datos_ordenados = sorted(array, key=lambda x: x[1])
    # Obtener los 3 más baratos (puedes ajustar este número según tus necesidades)
    mas_baratos = datos_ordenados[:valor]
    # Extraer solo las horas como strings
    horas_mas_baratas = [hora for hora, _ in mas_baratos]
    return horas_mas_baratas

# Devuelve la hora en el mismo formato que el primer valor de la tupla datos_ordenados para poder compararlos posteriormente


def hora_formatted():
    hora_actual_string = "2023-05-18 14:03:03"
    hora_actual_cutted = hora_actual_string[11:13]
    hora_siguiente = str(int(hora_actual_cutted) + 1)
    hora_actual_final = hora_actual_cutted + '-' + hora_siguiente
    return hora_actual_final


print(array_mas_baratos(prices_str, 3))
print("----------------\n")

# array de intervalos con las horas más baratas
print(obtener_horas_mas_baratas(datos_ordenados, 3))

print(hora_formatted())

for f in obtener_horas_mas_baratas(datos_ordenados, 3):
    if f == hora_formatted():
        print("La hora coincide")
    else:
        print(f"La hora {f} no coincide con {hora_formatted()}")

print("--------------------")
time = timecntrl.TimeController()
time.cargar_hora()
print(time.fecha_completa)
# print(time.hora_string)
# print(time.hora_intervalo)
print(time)

print("---------\n\n")

time = timecntrl.TimeController()
gpio = gpiocntrl.GPIOController()

if time.hora_intervalo in hora_formatted(): # debe estar encendido?
    gpio.es_hora = True
    if 

