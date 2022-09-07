import mysql
from CapaNegocio.database import *

class Persona (Database): #todas las clases inician con MAY
    def __init__(self):
        super().__init__()

    def getUnaPersona(self,id):
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

    def existepersona(self,IDCONDUCTOR):
        sql="SELECT * FROM tp4.Persona" WHERE ID_CONDUCTOR = '{}'".format (IDCONDUCTOR)
        persona=self.cursor.fetchone()
        return persona != None
### para probar cambios