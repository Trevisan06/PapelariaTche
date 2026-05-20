import mysql.connector
import sys
import os

# adiciona a pasta pai (Control) ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def exibir_dados_categoria():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM categoria")
        resultados = cursor.fetchall()

        print("\nCategoria:")

        for id_categoria, nome_categoria, descricao, setor, fileira, relevancia, cpf_cliente in resultados:
            print(f"ID: {id_categoria} | Nome: {nome_categoria} | Descrição: {descricao} | Setor: {setor} | Fileira: {fileira} | Relevância: {relevancia} | CPF Cliente: {cpf_cliente}")

        cursor.close()
        conexao.close()