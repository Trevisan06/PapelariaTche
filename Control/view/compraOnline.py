import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def exibir_compra_online():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM compraOnline")
        resultados = cursor.fetchall()

        print("\nCompra Online:")

        for cpf, nome, email, id, dataPedido, enderecoEntrega in resultados:
            print(f"CPF: {cpf} | Nome: {nome} | Email: {email} | ID Pedido: {id} | Data: {dataPedido} | Endereço: {enderecoEntrega}")

        cursor.close()
        conexao.close()