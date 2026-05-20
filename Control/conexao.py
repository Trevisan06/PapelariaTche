import mysql.connector

def conectar():
    
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="papelaria"
    )
    print("conectado")
    return conexao