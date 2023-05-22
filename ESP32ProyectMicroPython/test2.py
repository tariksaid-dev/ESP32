gmtime3 = 15
datos_ordenados = [('00-01', 98.33), ('01-02', 87.96), ('02-03', 86.84), ('03-04', 88.33), ('04-05', 100.84), ('05-06', 101.46), ('06-07', 101.63), ('07-08', 120.68), ('08-09', 129.74), ('09-10', 103.82), ('10-11', 140.01), ('11-12', 133.14),
                   ('12-13', 127.3), ('13-14', 118.58), ('14-15', 70.63), ('15-16', 71.11), ('16-17', 65.34), ('17-18', 71.58), ('18-19', 127.02), ('19-20', 140.55), ('20-21', 173.02), ('21-22', 200.29), ('22-23', 149.56), ('23-24', 133.84)]
def obtener_horas_mas_baratas(array, valor):
    # Ordenar por el segundo valor de la tupla
    datos_ordenados = sorted(array, key=lambda x: x[1])
    # Obtener los 3 más baratos (puedes ajustar este número según tus necesidades)
    mas_baratos = datos_ordenados[:valor]
    # Extraer solo las horas como strings
    horas_mas_baratas = [hora for hora, _ in mas_baratos]
    return horas_mas_baratas

print(obtener_horas_mas_baratas(datos_ordenados, 3))

valor = "06-07,07-08,08-09,09-10"
array_valor = valor.split(',')

print(array_valor)

