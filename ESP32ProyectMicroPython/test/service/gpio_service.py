import controller.gpio_controller as gpio
import controller.time_controller as time

class GPIOService:
  
  def comprobar_hora(self, array):
    if time.TimeController().hora_intervalo in array:
      gpio.GPIOController().es_hora = True
    else:
      gpio.GPIOController().es_hora = False

  def __init__(self):
    self.comprobar_hora()
    if gpio.GPIOController().es_hora:
      gpio.GPIOController().encender_todos()
      print("Se han encendido todos los GPIOS")
    else:
      gpio.GPIOController().apagar_todos()
      print("Se han apagado todos los GPIOS")

  def __str__(self):
    return (f"Los GPIOS están encendidos?: {gpio.GPIOController().esta_encendido}\nEs hora de que lo estén?: {gpio.GPIOController().es_hora}")





