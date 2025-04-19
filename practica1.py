class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

# Prueba
persona1 = Persona("Hector", 35)
persona1.presentarse()
