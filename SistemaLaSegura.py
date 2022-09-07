import sys
from PyQt5 import QtWidgets, uic
from CapaNegocio.coche import *
from CapaNegocio.persona import *
from CapaNegocio.accidente import * 
from datetime import date
import sys

class Iniciar:
    def __init__(self): 
        app=QtWidgets.QApplication([])
        self.ventana = uic.loadUi(r"C:\\Users\\david\\Desktop\\AX\\cosas de python\\Aseguradora\\LaSegura\\CapaVista\\VentanaPrincipal831.ui")
        self.ventana.show()
        ###conecta el menu con las funciones
        self.ventana.actionSALIR.triggered.connect(self.accionSalir)
        self.ventana.actionAUTOS.triggered.connect(self.accionCrudAutos)
        self.ventana.actionPERSONAS.triggered.connect(self.AccionCrudPersonas)
        self.ventana.actionACCIDENTE.triggered.connect(self.AccionCrudAccidentes)

        app.exec() # ejecuta la app
        
    #sys.exit
    def accionSalir(self):
        sys.exit()

    def accionCrudAutos(self):
        self.CrudAutos = uic.loadUi(r"C:\\Users\\david\\Desktop\\AX\\cosas de python\\Aseguradora\\LaSegura\\CapaVista\\CrudAuto.ui")
        self.CrudAutos.show() 
        #conectar los botones con las funciones
        self.CrudAutos.BtnAgregar.clicked.connect(self.Click_BtnAgregar)
        self.CrudAutos.BtnActualizar.clicked.connect(self.Click_BtnActualizar)
        self.CrudAutos.BtnBorrar.clicked.connect(self.Click_BtnBorrar)
        self.CrudAutos.BtnBuscar.clicked.connect(self.Click_BtnBuscar)
        self.CrudAutos.BtnCancelar.clicked.connect(self.Click_BtnCancelarAuto)
    
    def Click_BtnCancelarAuto (self):
        self.CrudAutos.close() 

    def Click_BtnAgregar(self):     
    #########obtener los valores de los imputs / line edit
        self.matricula= self.CrudAutos.InsertMatricula.text()        
        self.modelo= self.CrudAutos.InsertModelo.text()
        if self.verificarAnio (self.CrudAutos.InsertAnio.text()):
           self.Anio= int(self.CrudAutos.InsertAnio.text())
         
           if self.verificarMatricula(self.matricula) and self.verificarModelo (self.modelo) and self.verificarAnio(self.Anio):
              tcoche=coche()
              tcoche.insertcoche(self.matricula, self.modelo, self.Anio)
        else:
            self.CrudAutos.labeldisplay.setText("Inserte un Anio")
    
    def verificarMatricula (self,matricula): ####AGREGAR ACA LO QUE MANDO LA PROFE POR EMAIL##### 
        if matricula == "":
            self.CrudAutos.labeldisplay.setText ("INGRESAR UN MATRICULA")
            return False 
        else:
            return True

    def verificarModelo (self,modelo):
        if modelo == "":
            self.CrudAutos.labeldisplay.setText ("ingrese un modelo")
            return False 
        else:
            return True

    def verificarAnio (self,Anio):
        if Anio == "":
            self.CrudAutos.labeldisplay.setText ("ingrese un Anio")
            return False 
        elif  (int (Anio) <= date.today().year):
           return True
        else:
            return False

    def Click_BtnBorrar(self):
    #si en el texto de la mr no hay nada informar el error\
    # si hay algo pero no existe en la tabla informar que no existe
    # si existe borrarla
        self.matricula=self.CrudAutos.InsertMatricula.text()
        if self.verificarMatricula(self.matricula):
            if self.existeMatricula(self.matricula):
                tcoche=coche()
                tcoche.borrarcoche(self.matricula)
                self.CrudAutos.labeldisplay.setText ("EL COCHE SE BORRO")
            else:
                self.CrudAutos.labeldisplay.setText ("la matricula ingresada no existe en la base de datos")
        else:
             self.CrudAutos.labeldisplay.setText ("la matricula no se verifica")
    
    def existeMatricula(self,matricula): 
        cocheMatricula=coche()
        cocheMatricula.getUncoche(matricula)
        if cocheMatricula:
           return True 
        else:
            return False
    
  
    def Click_BtnActualizar(self):
        self.Anio=self.CrudAutos.InsertAnio.text()
        self.modelo=self.CrudAutos.InsertModelo.text()
        self.matricula=self.CrudAutos.InsertMatricula.text()
        if self.verificarMatricula(self.matricula):
            if self.existeMatricula(self.matricula):
                Actualizarcoche=coche()
                Actualizarcoche.updatecoche(self.Anio, self.modelo,self.matricula) 
                self.CrudAutos.labeldisplay.setText ("DATOS ACTUALIZADOS")
            else:
                self.CrudAutos.labeldisplay.setText ("LA MATRICULA INGRESADA NO EXISTE")
        else:
             self.CrudAutos.labeldisplay.setText ("NO ES POSIBLE VERIFICAR LA MATRICULA")

###############################################################################################
###############################################################################################

    # def Click_BtnBuscar(self): #busqueda secuencial
    #     self.Anio=self.CrudAutos.InsertAnio.text() 
    #     self.modelo=self.CrudAutos.InsertModelo.text() 
    #     self.matricula=self.CrudAutos.InsertMatricula.text()

    #     if self.existeMatricula(self.matricula):
    #         BuscarCocheMatricula=coche()
    #         BuscarCocheMatricula.getUncoche(self.matricula) 
    #             self.CrudAutos.labeldisplay.setText ("")
    #     else:
    #         self.CrudAutos.labeldisplay.setText ("No hay coincidencias")

    #     if self.existeModelo(self.matricula):
    #          BuscarCocheMatricula=coche()
    #           BuscarCocheMatricula.getUncoche(self.matricula) 
    #            self.CrudAutos.labeldisplay.setText ("")
    #     else:
    #         self.CrudAutos.labeldisplay.setText ("No hay coincidencias")

############################################################################################
############################################################################################
    def Click_BtnBuscar(self):    
        self.matricula=self.CrudAutos.InsertMatricula.text()
        if self.verificarMatricula(self.matricula):
         if self.existeMatricula(self.matricula):
            tauto=coche()
            auto = tauto.getUncoche(self.matricula)
            self.CrudAutos.InsertModelo.setText(auto[2])
            self.CrudAutos.InsertAnio.setText(auto[1])
            self.CrudAutos.labeldisplay.setText("El auto fue encontrado exitosamente")
         else:
            self.CrudAutos.labeldisplay.setText("La matrícula ingresada no existe en la Base de Datos")
        else:    
            self.CrudAutos.labeldisplay.setText("La matricula no se verifica")

##############################################################################################
#########################             CRUD PERSONA             ###############################


    def AccionCrudPersonas(self):
        self.CrudPersonas= uic.loadUi(r"C:\\Users\\david\\Desktop\\AX\\cosas de python\\Aseguradora\\LaSegura\\CapaVista\\CrudPersonas.ui")
        self.CrudPersonas.show() 
        #conectar los botones con las funciones
        self.CrudPersonas.BtnAgregarPersona.clicked.connect(self.Click_BtnAgregarPersona)
        self.CrudPersonas.BtnActualizarPersona.clicked.connect(self.Click_BtnActualizarPersona)
        self.CrudPersonas.BtnBorrarPersona.clicked.connect(self.Click_BtnBorrarPersona)
        self.CrudPersonas.BtnBuscarPersona.clicked.connect(self.Click_BtnBuscarPersona)
        self.CrudPersonas.BtnCancelar.clicked.connect(self.Click_BtnCancelarPersona)
        
    def Click_BtnCancelarPersona(self):
        self.CrudPersonas.close() 

    def Click_BtnAgregarPersona(self):     
    #########obtener los valores de los imputs / line edit
        self.ID= self.CrudPersonas.InsertIDPersona.text()        
        self.NOMBRE= self.CrudPersonas.InsertNombrePersona.text()
        self.APELLIDO= self.CrudPersonas.InsertApellidoPersona.text()
        self.DIRECCION= self.CrudPersonas.InsertDireccionPersona.text()
        NuevaPersona=Persona() 
        NuevaPersona.insertPersona(self.ID,self.NOMBRE, self.APELLIDO, self.DIRECCION)

    def Click_BtnBorrarPersona(self):
        self.ID= self.CrudPersonas.InsertIDPersona.text()   
        if self.verificarID (self.ID):
                Lapersona=Persona()
                Lapersona.borrarPersona(self.ID)
                self.CrudPersonas.labeldisplay.setText ("SE BORRO LA PERSONA")
        else:
             self.CrudPersonas.labeldisplay.setText ("El ID ingresado no corresponde a ninguna persona")
    
    def verificarID (self,ID): ####HACER LO DE EXPRESIONES REGULARES
        if ID == "":
           self.CrudPersonas.labeldisplay.setText ("INGRESE UN ID")
           return False 
        else:
            return True

    def Click_BtnActualizarPersona(self):
        self.ID= self.CrudPersonas.InsertIDPersona.text()        
        self.NOMBRE= self.CrudPersonas.InsertNombrePersona.text()
        self.APELLIDO= self.CrudPersonas.InsertApellidoPersona.text()
        self.DIRECCION= self.CrudPersonas.InsertDireccionPersona.text()

        if self.verificarID(self.ID):
           ActualizarPersona=Persona()
           ActualizarPersona.updatePersona(self.NOMBRE,self.APELLIDO,self.DIRECCION,self.ID) 
           self.CrudPersonas.labeldisplay.setText ("DATOS ACTUALIZADOS")
        else:
             self.CrudPersonas.labeldisplay.setText ("ID NO EXISTE, INGRESE UN ID VALIDO")
     
    def Click_BtnBuscarPersona(self):    
        self.ID=self.CrudPersonas.InsertIDPersona.text()  
        if self.verificarID(self.ID):
           BuscarPersona=Persona()
           PersonaBuscada= BuscarPersona.getUnaPersona(self.ID)
           self.CrudPersonas.InsertNombrePersona.setText(PersonaBuscada[1])
           self.CrudPersonas.InsertApellidoPersona.setText(PersonaBuscada[2])
           self.CrudPersonas.InsertDireccionPersona.setText(PersonaBuscada[3])
           self.CrudPersonas.labeldisplay.setText ("ID NO EXISTE, INGRESE UN ID VALIDO")
           self.CrudPersonas.labeldisplay.setText("PERSONA ENCONTRADA")
        else:
             self.CrudPersonas.labeldisplay.setText ("ID NO EXISTE, INGRESE UN ID VALIDO")
             self.CrudPersonas.label.setText("ID NO EXISTE, INGRESE UN ID VALIDO")

############################################################################################
# ############################### CRUD ACCIDENTE ###########################################    
#  
    def AccionCrudAccidentes(self):
        
        self.CrudAccidentes = uic.loadUi(r"C:\\Users\\david\\Desktop\\AX\\cosas de python\\Aseguradora\\LaSegura\\CapaVista\\CrudAccidente.ui")
        self.CrudAutos.show() 
        #conectar los botones con las funciones
        self.CrudAutos.BtnAgregar.clicked.connect(self.Click_BtnAgregar)
        self.CrudAutos.BtnActualizar.clicked.connect(self.Click_BtnActualizar)
        self.CrudAutos.BtnBorrar.clicked.connect(self.Click_BtnBorrar)
        self.CrudAutos.BtnBuscar.clicked.connect(self.Click_BtnBuscar)
        self.CrudAutos.BtnCancelar.clicked.connect(self.Click_BtnCancelarAuto)
    
Iniciar()
