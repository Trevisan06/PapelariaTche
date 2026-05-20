import mysql.connector
import sys
import os

# adiciona a pasta pai (Control) ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def exibir_dados_compra():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM compra")
        resultados = cursor.fetchall()

        print("\nCompra:")

        for id_compra, data_compra, valor_compra, forma_pagamento, quantidade_itens, id_funcionario, cod_produto in resultados:
            print(f"ID: {id_compra} | Data: {data_compra} | Valor: {valor_compra} | Pagamento: {forma_pagamento} | Quantidade itens: {quantidade_itens} | ID Funcionário: {id_funcionario} | Código Produto: {cod_produto}")

        cursor.close()
        conexao.close()