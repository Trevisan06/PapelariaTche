import mysql.connector
import sys
import os

# adiciona a pasta pai (Control) ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def exibir_dados_clientes():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT nome, dataNascimento, pontos, contato, email FROM clientes")
        resultados = cursor.fetchall()

        print("\nClientes:")

        for nome, data_nascimento, pontos, contato, email in resultados:
            print(f"Nome: {nome} | Data nascimento: {data_nascimento} | Pontos: {pontos} | Contato: {contato} | Email: {email}")

        cursor.close()
        conexao.close()
