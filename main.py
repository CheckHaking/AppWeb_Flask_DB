#Levantaremos el servider web con Flask
from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea

app = Flask(__name__)

@app.route('/')
def home():
    get_all_task = db.session.query(Tarea).all()
    #for i in get_all_task:
        #print(i)

    return render_template('index.html', task_list=get_all_task)
@app.route('/crear-tarea', methods=["POST"])
def crearTarea():
    tarea = Tarea(contenido=request.form["contenido_tarea"], done=False)
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/delete-task/<id>')
def delete(id):
    task = db.session.query(Tarea).filter_by(id=int(id))
    task.delete()
    db.session.commit()
    return redirect(url_for('home'))


def crear():
    pass


if __name__ == "__main__":
    #indicamos que se creen las tablas de todos los modulos que encuentre en models.py
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)