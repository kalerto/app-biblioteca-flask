class Libro:
    """
    Representa un libro con un título, autor y año de publicación.
    """
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar_info(self):
        """
        Muestra la información del libro en un formato legible.
        """
        return f"{self.titulo} de {self.autor} ({self.anio})"

class Biblioteca:
    """
    Representa una biblioteca que puede almacenar libros.
    """
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        """
        Agrega un libro a la biblioteca.
        """
        self.libros.append(libro)

    def mostrar_libros(self):
        """
        Muestra todos los libros almacenados en la biblioteca.
        """
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            for libro in self.libros:
                print(libro.mostrar_info())

# Creamos algunos libros
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
libro2 = Libro("1984", "George Orwell", 1949)

# Creamos la biblioteca
mi_biblioteca = Biblioteca()

# Agregamos los libros
mi_biblioteca.agregar_libro(libro1)
mi_biblioteca.agregar_libro(libro2)

# Mostramos los libros
mi_biblioteca.mostrar_libros()
