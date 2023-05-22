from machine import Pin
import _thread

class GPIOController:
    def __init__(self):
        # Inicializar los pines GPIO según tus necesidades {32, 25, 27, 14}.
        self.gpio1 = Pin(32, Pin.OUT)
        self.gpio2 = Pin(25, Pin.OUT)
        self.gpio3 = Pin(27, Pin.OUT)
        self.gpio4 = Pin(14, Pin.OUT)
        self.esta_encendido = False
        self.es_hora = False

    # Encendiendo
    def encender_todos(self):
        if not self.esta_encendido:
            self.gpio1.value(1)
            self.gpio2.value(1)
            self.gpio3.value(1)
            self.gpio4.value(1)
            self.esta_encendido = True
        else:
            print("No se puede encender, ya que ya está encendido")

    def encender_gpio_32(self):
        self.gpio1.value(1)

    def encender_gpio_25(self):
        self.gpio2.value(1)

    def encender_gpio_27(self):
        self.gpio3.value(1)

    def encender_gpio_14(self):
        self.gpio4.value(1)

    # Apagando
    def apagar_todos(self):
        if self.esta_encendido:
            self.gpio1.value(0)
            self.gpio2.value(0)
            self.gpio3.value(0)
            self.gpio4.value(0)
            self.esta_encendido = False
        else:
            print("No se puede apagar ya que ya esta apagado")
            
    def apagar_gpio_32(self):
        self.gpio1.value(0)

    def apagar_gpio_25(self):
        self.gpio2.value(0)

    def apagar_gpio_27(self):
        self.gpio3.value(0)

    def apagar_gpio_14(self):
        self.gpio4.value(0)

    def test_on(self):
        pin = Pin(17, Pin.OUT) # Primer argumento nº del pin, segundo tarea de output.
        pin.value(1) # 1 = electricidad, 0 = parao

    def test_off(self):
        pin = Pin(17, Pin.OUT) # Primer argumento nº del pin, segundo tarea de output.
        pin.value(0) # 1 = electricidad, 0 = parao