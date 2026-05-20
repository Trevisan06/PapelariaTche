import mysql.connector
import sys
import os

# adiciona a pasta pai (Control) ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_dados_promocao():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        nome = input("Nome da promoção: ")
        desconto = int(input("Desconto: "))
        dataInicio = input("Data de início: ")
        dataFim = input("Data de fim: ")
        motivo = input("Motivo: ")
        codProduto = int(input("Código do produto: "))

        sql = "INSERT INTO promocao (nome, desconto, dataInicio, dataFim, motivo, codProduto) VALUES (%s, %s, %s, %s, %s, %s)"

        values = (nome, desconto, dataInicio, dataFim, motivo, codProduto)

        cursor.execute(sql, values)
        conexao.commit()

        print("Promoção inserida")

        cursor.close()
        conexao.close()