
from sqlalchemy import Column, Integer, String, Boolean

import db

class Tarea(db.Base):

    __tablename__ = "tarea"
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True)
    contenido = Column(String(200), nullable=False)
    done = Column(Boolean)

    def __init__(self, contenido, done):
        self.contenido = contenido
        self.done = done
        print('Tarea Creada con Exito!')

    def __str__(self):
        return """Tarea: ({}: {} ({}))""".format(self.id, self.contenido, self.done)



