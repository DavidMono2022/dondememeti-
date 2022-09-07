import mysql
from CapaNegocio.database import *
from CapaNegocio.Persona import *
from CapaNegocio.coche import *
from CapaNegocio.accidente import *

class vincular (database): # 
    def __init__(self):
        super(). __init__()
    
    def vincularPersona(self,ID_CONDUCTOR,COCHE_MATRICULA,ACCIDENTE_NRO_INFORME):
        #VERIFICAR QUE LA PERSONA EXISTE EN LA BASE DE DATOS
        #VERIFICAR QUE EL AUTO EXISTE EN LA BASE DE DATOS
        #INSERTAR EN TABLA ACCIDENTE
        persona=Persona()
        coche=coche()
        if perona.existePersona(ID_CONDUCTOR):
           if coche.getUnCoche(COCHE_MATRICULA) != None
             sql="INSERT INTO tp4.persona_has_coche VALUES ({},'{}')". FORMAT (ID_CONDUCTOR,COCHE_MATRICULA)
             self.cursor.executr(sql)
             self.cursos.commint()
             return "se inserto exitosamente"
            else:
             return "la matriculka no existe"
        else:
            return "la persona no existe"
    
    def  vincularAutoInforme (self,COCHE_MATRICULA,ACCIDENTE_NRO_INFORME):
         #VERIFICAR SI EXISTR EL AUTO, Y TRAER EL CONDUCTOR ASOCIADO
         #VERIFICAR SI EXISTE INFORME
         #INSERTAR EN LA TABLA CORRESPONDIENTE
        persona=Persona()
        Uncoche=coche()
        Unaccidente=accidente()
        if coche.getUnCoche(COCHE_MATRICULA) != None:
            ID_CONDUCTOR=TraerIDCONDUCTOR(COCHE_MATRICULA)
            if Unaccidente.getInforme(ACCIDENTE_NRO_INFORME) !=None:
                sql="INSERT INTO tp4.accidente_has_persona_has_coche "
                self.cursor.execute(sql)
                self.cursor.commit()
                return "se inserto exitosamente"
            else:
                return "el auto no tiene conduxtor asignado"
        else:
            return "la matricula no existe"

    def traerIDCONDUCTOR (self,COCHE_MATRICULA):
        sql="SELECT persona.ID_CONDUCTOR * FROM tp4.persona_has_coche WHERE COCHE_MATRÍCULA= '{}'".format (COCHE_MATRICULA)
        self.cursor.execute(sql)
        return self.cursor.fetchone()
       



        


    def getUnVinculo(IDPERSONA,):
        sql="SELECT * FROM tp4.Persona WHERE ID_CONDUCTOR={}".format(id)
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    
    def getTodasLasPersona(self):
        sql="SELECT * FROM tp4.Persona"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def insertPersona(self,id,nombre,apellido,direccion):
        sql="INSERT INTO  tp4.persona VALUES ('{}',{},'{}')".format(id,nombre,apellido,direccion)
        self.cursor.execute(sql)
        self.connection.commit() #para insert, delete,,,,,,

    def updatePersona(self,nombre,apellido,direccion,id):
        sql="UPDATE tp4.persona SET PERSONA_NOMBRE = '{}', PERSONA_APELLIDO = '{}', PERSONA_DIRECCIÓN = '{}' WHERE ID_CONDUCTOR={}".format(nombre,apellido,direccion,id)
        self.cursor.execute(sql) #UPDATE `tp4`.`persona`SET PERSONA_NOMBRE='MIGUEL ANGEL',PERSONA_APELLIDO='GARCIAS',PERSONA_DIRECCIÓN='COLON Y LUIGGI' WHERE ID_CONDUCTOR=998;
        self.connection.commit()
    
    def borrarPersona(self,id):
        sql="DELETE FROM tp4.Persona WHERE ID_CONDUCTOR={}".format(id)
        self.cursor.execute(sql)
        self.connection.commit()
