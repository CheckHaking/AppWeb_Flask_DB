#Levantaremos el servider web con Flask
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    #Portada de la pagina
    #Retornar un fichero HTML
    return render_template('index.html')
@app.route('/crear-tarea')
def crearTarea():
    return 'Crear Tarea'


if __name__ == "__main__":
    app.run(debug=True)