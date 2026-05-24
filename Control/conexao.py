import mysql.connector

def conectar():
    
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="08062008VM",
        database="papelaria"
    )
    print("conectado")
    return conexao