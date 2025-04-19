from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Definimos la clase Libro y la Biblioteca
class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def mostrar_info(self):
        return f"{self.titulo} de {self.autor} ({self.anio})"


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, titulo):
        self.libros = [libro for libro in self.libros if libro.titulo != titulo]

    def editar_libro(self, viejo_titulo, nuevo_titulo, nuevo_autor, nuevo_anio):
        for libro in self.libros:
            if libro.titulo == viejo_titulo:
                libro.titulo = nuevo_titulo
                libro.autor = nuevo_autor
                libro.anio = nuevo_anio
                break

    def mostrar_libros(self):
        return self.libros

# Crear una instancia de la biblioteca
mi_biblioteca = Biblioteca()

@app.route('/')
def index():
    # Mostramos los libros en la página principal
    return render_template('index.html', libros=mi_biblioteca.mostrar_libros())

@app.route('/agregar', methods=['POST'])
def agregar():
    titulo = request.form['titulo']
    autor = request.form['autor']
    anio = int(request.form['anio'])
    libro = Libro(titulo, autor, anio)
    mi_biblioteca.agregar_libro(libro)
    return redirect(url_for('index'))

@app.route('/eliminar/<titulo>')
def eliminar(titulo):
    mi_biblioteca.eliminar_libro(titulo)
    return redirect(url_for('index'))

@app.route('/editar/<titulo>', methods=['GET', 'POST'])
def editar(titulo):
    if request.method == 'POST':
        nuevo_titulo = request.form['titulo']
        nuevo_autor = request.form['autor']
        nuevo_anio = int(request.form['anio'])
        mi_biblioteca.editar_libro(titulo, nuevo_titulo, nuevo_autor, nuevo_anio)
        return redirect(url_for('index'))
    else:
        return render_template('editar.html', titulo=titulo)

if __name__ == '__main__':
    app.run(debug=True)
