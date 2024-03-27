#Levantaremos el servider web con Flask
from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea

app = Flask(__name__)

@app.route('/')
def home():
    get_all_task = db.session.query(Tarea).all()
    get_all_task_done = db.session.query(Tarea).filter_by(done=1).all()
    task_done = len(get_all_task_done)
    total_tasks = len(get_all_task)
    if total_tasks !=0:
        progress = round((task_done*100)/total_tasks)
    else: progress = 0


    print('READY==>',progress)
    return render_template('index.html', task_list=get_all_task, progress=progress)
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

@app.route('/task-done/<id>')
def done(id):
    task = db.session.query(Tarea).filter_by(id=int(id)).first()
    task.done = not(task.done)
    db.session.commit()
    return redirect(url_for('home'))




if __name__ == "__main__":
    #indicamos que se creen las tablas de todos los modulos que encuentre en models.py
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)