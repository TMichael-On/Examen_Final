
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
        #aux=int(self.valida(self.txtId.text()))
        aux=int(self.txtId.text())
        mensaje = "null"
        aux1=0
        for item in mostrar:
            if item.idAsignatura == aux:
                ID = item.idAsignatura
                Nombre = item.nombreAsignatura
                self.lblCod.setText(ID.__str__())
                self.lblNomb.setText(Nombre.__str__())
                aux1=1
        if aux1==1:
            mensaje="Registro encontrado"
        else:
            mensaje = "ERROR: \t Registro no encontrado"
            self.lblCod.setText("________________________________________".__str__())
            self.lblNomb.setText("________________________________________".__str__())
        self.txtMensaje.setText(mensaje.__str__())

    def editar_asignatura(self):

        id = self.lblCod.text()
        nombre = self.leANombre.text()
        mensaje = "null"

        busqueda = session.query(Asignatura).filter(Asignatura.nombreAsignatura == nombre,
                                                    Asignatura.idAsignatura != id).all()
        if len(busqueda) == 0:
            asignatura = session.query(Asignatura).filter(Asignatura.idAsignatura == id).first()
            asignatura.nombreAsignatura = nombre
            session.commit()
            mensaje = "Se actualizó el registro."
        else:
            mensaje = "Ya existe el titulo. No se actualizó el registro."
        self.txtMensaje.setText(mensaje.__str__())


    def exit_app(self):
        resultado = messagebox.askquestion("Salir", "¿Está seguro que desea salir?")
        if resultado == "yes":
            quit(0)


    def valida (cadena):
        for validate in cadena:
            if validate.isdigit():
                cadena=int(cadena)
            else:
                print("Error Cadena | Valida")
                #Editar()
                # resultado = messagebox.askquestion("Salir", "¿Está seguro que desea salir?")
                cadena=0
        return cadena