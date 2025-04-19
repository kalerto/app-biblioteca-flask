class Coche:
    def __init__(self, marca):
        self.marca = marca
        self.encendido = False

    def encender(self):
        self.encendido = True
        print("Coche encendido.")

    def apagar(self):
        self.encendido = False
        print("Coche apagado.")

    def estado(self):
        print(f"El coche está {'encendido' if self.encendido else 'apagado'}.")

# Prueba
mi_coche = Coche("Toyota")
mi_coche.estado()
mi_coche.encender()
mi_coche.estado()
