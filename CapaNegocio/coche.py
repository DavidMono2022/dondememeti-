import mysql
from CapaNegocio.database import *

class coche (Database): #todas las clases inician con MAY
    def __init__(self):
        super().__init__() # los cambios se quedan senialados con la M

    def getUncoche(self,matricula):
        sql="SELECT * from tp4.coche WHERE COCHE_MATRÍCULA='{}'".format(matricula) # COPIAR EL SELECT DIRECTAMENTE
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    
    def getTodosLoscoches(self):
        sql="SELECT * FROM tp4.coche"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def insertcoche(self,matricula,modelo,AÑO):
        sql="INSERT INTO  tp4.coche VALUES ('{}',{},'{}')".format(matricula,AÑO,modelo)
        self.cursor.execute(sql)
        self.connection.commit() #para insert, delete,,,,,,

    def updatecoche(self,AÑO,modelo,matricula):
        sql="UPDATE tp4.coche SET COCHE_AÑO= {}, COCHE_MODELO= '{}' WHERE COCHE_MATRÍCULA = '{}'".format(AÑO,modelo,matricula)
        self.cursor.execute(sql)
        self.connection.commit()
    
    def borrarcoche(self,matricula):
        sql="DELETE FROM tp4.coche WHERE COCHE_MATRÍCULA ='{}'".format(matricula)
        self.cursor.execute(sql)
        self.connection.commit()