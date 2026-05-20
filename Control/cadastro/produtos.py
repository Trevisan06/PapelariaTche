import mysql.connector
import sys
import os

# adiciona a pasta pai (Control) ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_dados_produtos():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        quantidadeEstoque = int(input("Quantidade em estoque: "))
        marca = input("Marca: ")
        validade = input("Validade: ")
        categoria = int(input("ID da categoria: "))

        sql = "INSERT INTO produtos (nome, preco, quantidadeEstoque, marca, validade,categoria) VALUES (%s, %s, %s, %s, %s, %s)"

        values = (nome, preco, quantidadeEstoque, marca, validade, categoria)

        cursor.execute(sql, values)
        conexao.commit()

        print("Produto inserido")

        cursor.close()
        conexao.close()