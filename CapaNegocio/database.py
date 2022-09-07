import pymysql
class Database:
    # Genero la apertura y cierre con la Base de Datos 
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Curso@X2022',
            db='tp4'
        )
        self.cursor=self.connection.cursor() 
        print("Conexion establecida")

    def close(self):
       self.connection.close