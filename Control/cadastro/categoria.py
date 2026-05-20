import mysql.connector
import sys
import os

# adiciona a pasta pai (Control) ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_dados_categoria():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        nome_categoria = input("Nome da categoria: ")
        descricao = input("Descrição: ")
        setor = input("Setor: ")
        fileira = int(input("Fileira: "))
        relevancia = input("Relevância: ")
        cpf_cliente = int(input("CPF do cliente: "))

        sql = "INSERT INTO categoria (nomeCategoria, descricao, setor, fileira, relevancia, cpfCliente) VALUES (%s, %s, %s, %s, %s, %s)"

        values = (nome_categoria, descricao, setor, fileira, relevancia, cpf_cliente)

        cursor.execute(sql, values)
        conexao.commit()

        print("Categoria inserida")

        cursor.close()
        conexao.close()