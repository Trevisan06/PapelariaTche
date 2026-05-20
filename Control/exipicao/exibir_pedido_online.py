import mysql.connector
import sys
import os

# adiciona a pasta pai (Control) ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def exibir_dados_pedido_online():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM pedidoOnline")
        resultados = cursor.fetchall()

        print("\nPedido Online:")

        for id_pedido, data_pedido, valor_pedido, forma_entrega, status_entrega, endereco_entrega, cpf_cliente in resultados:
            print(f"ID: {id_pedido} | Data: {data_pedido} | Valor: {valor_pedido} | Forma entrega: {forma_entrega} | Status: {status_entrega} | Endereço: {endereco_entrega} | CPF Cliente: {cpf_cliente}")

        cursor.close()
        conexao.close()