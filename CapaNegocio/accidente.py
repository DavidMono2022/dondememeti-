import mysql
from CapaNegocio.database import *

class accidente (Database): #todas las clases inician con MAY
    def __init__(self):
        super().__init__()

    def getUnAccidente(self,ACCIDENTE_NRO_INFORME):
        sql="SELECT * from tp4.accidente WHERE ACCIDENTE_NRO_INFORME='{}'".format(ACCIDENTE_NRO_INFORME) 
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    
    def getTodosLosAccidentes(self):
        sql="SELECT * FROM tp4.accidente"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def insertAccidente(self,ACCIDENTE_NRO_INFORME, ACCIDENTE_FECHA, ACCIDENTE_LUGAR):
        sql="INSERT INTO  tp4.accidente VALUES ({},'{}','{}')".format(ACCIDENTE_NRO_INFORME, ACCIDENTE_FECHA, ACCIDENTE_LUGAR)
        self.cursor.execute(sql)
        self.connection.commit() 

    # def insertInforme (self,IDinforme,fecha,lugar)
    # sql="INSERT INTO TP4.informeaccidente VALUES ({},'{}','{}'".format(IDinforme,fecha,lugar)
    #self.cursor.execute(sql)
    #self.connection.commit() 
    #return "informe insertado exitosamente"
       

    def updateAccidente(self,ACCIDENTE_NRO_INFORME, ACCIDENTE_FECHA, ACCIDENTE_LUGAR, ID_CONDUCTOR):
        sql="UPDATE tp4.accidente SET ACCIDENTE_NRO_INFORME= {}, ACCIDENTE_FECHA= '{}', ACCIDENTE_LUGAR='{}', ID_CONDUCTOR = {} WHERE ACCIDENTE_NRO_INFORME = {}".format(ACCIDENTE_NRO_INFORME, ACCIDENTE_FECHA, ACCIDENTE_LUGAR, ID_CONDUCTOR)
        self.cursor.execute(sql)
        self.connection.commit()
    
    def borrarAccidente(self,ACCIDENTE_NRO_INFORME):
        sql="DELETE FROM tp4.accidente WHERE ACCIDENTE_NRO_INFORME ={}".format(ACCIDENTE_NRO_INFORME)
        self.cursor.execute(sql)
        self.connection.commit()