from src.seleccionestudiante.modelo.Asignatura import Asignatura
from src.seleccionestudiante.modelo.declarative_base import engine, Base, session


#engine = create_engine('sqlite:///aplicacion2.sqlite')
#Base = declarative_base()

if __name__ == '__main__':

    mostrar = session.query(Asignatura).all()
    print(mostrar)
    for item in mostrar:
        if item.idAsignatura == 1:
            A = item.nombreAsignatura
            print(A)