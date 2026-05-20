import mysql.connector
import sys
import os

# adiciona a pasta pai (Control) ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_dados_parcelas():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        numeroParcela = int(input("Número da parcela: "))
        valorParcela = float(input("Valor da parcela: "))
        dataVencimento = input("Data de vencimento: ")
        dataPagamento = input("Data de pagamento: ")
        statusParcela = input("Status da parcela: ")

        sql = "INSERT INTO parcelas (numeroParcela, valorParcela, dataVencimento, dataPagamento, statusParcela) VALUES (%s, %s, %s, %s, %s)"

        values = (numero_parcela, valor_parcela, data_vencimento, data_pagamento, status_parcela)

        cursor.execute(sql, values)
        conexao.commit()

        print("Parcela inserida")

        cursor.close()
        conexao.close()