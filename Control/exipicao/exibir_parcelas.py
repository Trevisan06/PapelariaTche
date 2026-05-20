import mysql.connector
import sys
import os

# adiciona a pasta pai (Control) ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def exibir_dados_parcelas():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM parcelas")
        resultados = cursor.fetchall()

        print("\nParcelas:")

        for cod_parcelas, numero_parcela, valor_parcela, data_vencimento, data_pagamento, status_parcela, id_pedido in resultados:
            print(f"Código: {cod_parcelas} | Número parcela: {numero_parcela} | Valor: {valor_parcela} | Vencimento: {data_vencimento} | Pagamento: {data_pagamento} | Status: {status_parcela} | ID Pedido: {id_pedido}")

        cursor.close()
        conexao.close()