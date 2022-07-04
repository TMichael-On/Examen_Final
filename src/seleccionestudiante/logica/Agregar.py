
from src.seleccionestudiante.modelo.Asignatura import Asignatura
from src.seleccionestudiante.modelo.declarative_base import engine, Base, session

class Agregar():

    def __init__(self):
        Base.metadata.create_all(engine)
        #ruta = os.path.dirname(os.path.abspath(__file__)) + r"\src\seleccionestudiante\vista\Prueba.ui"
        #QDialog.__init__(self)
        #uic.loadUi(ruta, self)


    def agregar_asignatura(self, nombreAsignatura):
        busqueda = session.query(Asignatura).filter(Asignatura.nombreAsignatura == nombreAsignatura).all()
        if len(busqueda) == 0:
            asignatura = Asignatura(nombreAsignatura=nombreAsignatura)
            session.add(asignatura)
            session.commit()
            return True
        else:
            return False