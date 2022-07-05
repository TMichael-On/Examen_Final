import sys
import os

from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6 import uic
from tkinter import messagebox

from src.seleccionestudiante.modelo.Asignatura import Asignatura
from src.seleccionestudiante.modelo.declarative_base import engine, Base, session

class Editar(QDialog):

    def __init__(self):

        ruta = os.path.dirname(os.path.abspath(__file__)) + r"\..\vista\EditarAsignatura.ui"
        QDialog.__init__(self)
        uic.loadUi(ruta, self)

        self.btnEditar.clicked.connect(self.mostrar_datos)
        self.btnAceptar.clicked.connect(self.editar_asignatura)
        self.btnCancelar.clicked.connect(self.exit_app)

    def mostrar_datos(self):
        mostrar = session.query(Asignatura).all()

        for item in mostrar:
            if item.idAsignatura == int(self.txtId.text()):
                ID = item.idAsignatura
                Nombre = item.nombreAsignatura

                self.lblCod.setText(ID.__str__())
                self.lblNomb.setText(Nombre.__str__())
                #print(ID,Nombre)
        #self.lblCod.setText(mostrar.nombreAsignatura)
        #self.leANombre.setText(mostrar.nombreAsignatura)
        #session.close()

    def editar_asignatura(self):

        id = self.lblCod.text()
        nombre = self.leANombre.text()
        #estudiante_ = ""
        mensaje = "null"

        busqueda = session.query(Asignatura).filter(Asignatura.nombreAsignatura == nombre,
                                                    Asignatura.idAsignatura != id).all()
        if len(busqueda) == 0:
            asignatura = session.query(Asignatura).filter(Asignatura.idAsignatura == id).first()
            asignatura.nombreAsignatura = nombre
            # asignatura.estudiantes = estudiante_
            session.commit()
            mensaje = "Se actualizó el registro."
        else:
            mensaje = "Ya existe el titulo. No se actualizó el registro."
        self.txtMensaje.setText(mensaje)
        print(id,nombre)

    def exit_app(self):
        resultado = messagebox.askquestion("Salir", "¿Está seguro que desea salir?")
        if resultado == "yes":
            # exit(0)
            quit(0)