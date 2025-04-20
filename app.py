
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biblioteca.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    autor = db.Column(db.String(200), nullable=False)
    anio = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Libro('{self.titulo}', '{self.autor}', {self.anio})"

@app.route('/')
def index():
    libros = Libro.query.all()
    return render_template('index.html', libros=libros)

@app.route('/agregar', methods=['POST'])
def agregar():
    titulo = request.form['titulo']
    autor = request.form['autor']
    anio = int(request.form['anio'])
    nuevo_libro = Libro(titulo=titulo, autor=autor, anio=anio)
    db.session.add(nuevo_libro)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/eliminar/<int:id>')
def eliminar(id):
    libro = Libro.query.get_or_404(id)
    db.session.delete(libro)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    libro = Libro.query.get_or_404(id)
    if request.method == 'POST':
        libro.titulo = request.form['titulo']
        libro.autor = request.form['autor']
        libro.anio = int(request.form['anio'])
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editar.html', libro=libro)

if __name__ == '__main__':
    app.run(debug=True)
