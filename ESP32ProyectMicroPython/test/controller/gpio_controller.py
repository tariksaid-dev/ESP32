from machine import Pin

class GPIOController:
    def __init__(self):
        # Inicializar los pines GPIO según tus necesidades {32, 25, 27, 14}.
        self.gpio1 = Pin(32, Pin.OUT)
        self.gpio2 = Pin(25, Pin.OUT)
        self.gpio3 = Pin(27, Pin.OUT)
        self.gpio4 = Pin(14, Pin.OUT)

    # Encendiendo
    def encender_todos(self):
        self.gpio1.value(1)
        self.gpio2.value(1)
        self.gpio3.value(1)
        self.gpio4.value(1)

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
        self.gpio1.value(0)
        self.gpio2.value(0)
        self.gpio3.value(0)
        self.gpio4.value(0)

    def apagar_gpio_32(self):
        self.gpio1.value(0)

    def apagar_gpio_25(self):
        self.gpio2.value(0)

    def apagar_gpio_27(self):
        self.gpio3.value(0)

    def apagar_gpio_14(self):
        self.gpio4.value(0)
