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

    def editar(self, titulo=None, autor=None, anio=None):
        """
        Permite editar el libro. Si no se pasa un valor, no se modifica.
        """
        if titulo:
            self.titulo = titulo
        if autor:
            self.autor = autor
        if anio:
            self.anio = anio


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

    def eliminar_libro(self, titulo):
        """
        Elimina un libro de la biblioteca por su título.
        """
        for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)
                print(f"El libro '{titulo}' ha sido eliminado.")
                return
        print(f"No se encontró un libro con el título '{titulo}'.")

    def mostrar_libros(self):
        """
        Muestra todos los libros almacenados en la biblioteca.
        """
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            for libro in self.libros:
                print(libro.mostrar_info())

    def buscar_libro(self, titulo):
        """
        Busca un libro por su título.
        """
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None


# Función para pedir datos al usuario y agregar un libro
def agregar_libro_por_usuario(biblioteca):
    print("Introduce los datos del libro:")
    titulo = input("Título del libro: ")
    autor = input("Autor del libro: ")
    anio = input("Año de publicación: ")

    # Verificar que el año sea un número
    while not anio.isdigit():
        print("Por favor, introduce un año válido.")
        anio = input("Año de publicación: ")

    # Crear el libro y agregarlo a la biblioteca
    libro = Libro(titulo, autor, int(anio))
    biblioteca.agregar_libro(libro)
    print(f"Se ha agregado el libro: {libro.mostrar_info()}")

# Función para editar un libro
def editar_libro(biblioteca):
    titulo = input("Introduce el título del libro que deseas editar: ")
    libro = biblioteca.buscar_libro(titulo)

    if libro:
        print("Introduce los nuevos datos del libro (deja en blanco para no modificar):")
        nuevo_titulo = input(f"Título (actual: {libro.titulo}): ")
        nuevo_autor = input(f"Autor (actual: {libro.autor}): ")
        nuevo_anio = input(f"Año (actual: {libro.anio}): ")

        libro.editar(
            titulo=nuevo_titulo if nuevo_titulo else None,
            autor=nuevo_autor if nuevo_autor else None,
            anio=int(nuevo_anio) if nuevo_anio else None
        )
        print(f"El libro ha sido actualizado: {libro.mostrar_info()}")
    else:
        print("No se encontró un libro con ese título.")

# Función para eliminar un libro
def eliminar_libro(biblioteca):
    titulo = input("Introduce el título del libro que deseas eliminar: ")
    biblioteca.eliminar_libro(titulo)


# Función principal que ejecuta el menú interactivo
def menu(biblioteca):
    while True:
        print("\nMenú de la Biblioteca:")
        print("1. Agregar libro")
        print("2. Editar libro")
        print("3. Eliminar libro")
        print("4. Mostrar libros")
        print("5. Salir (FIN)")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_libro_por_usuario(biblioteca)
        elif opcion == "2":
            editar_libro(biblioteca)
        elif opcion == "3":
            eliminar_libro(biblioteca)
        elif opcion == "4":
            biblioteca.mostrar_libros()
        elif opcion.lower() == "fin":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Crear la biblioteca
mi_biblioteca = Biblioteca()

# Ejecutar el menú
menu(mi_biblioteca)
