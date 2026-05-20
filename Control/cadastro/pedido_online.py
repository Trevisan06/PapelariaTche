import mysql.connector
import sys
import os

# adiciona a pasta pai (Control) ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_dados_pedido_online():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        dataPedido = input("Data do pedido: ")
        valorPedido = float(input("Valor do pedido: "))
        formaEntrega = input("Forma de entrega: ")
        statusEntrega = input("Status da entrega: ")
        enderecoEntrega = input("Endereço da entrega: ")
        cpf_cliente = int(input("CPF do cliente: "))

        sql = "INSERT INTO pedidoOnline (dataPedido, valorPedido, formaEntrega, statusEntrega, enderecoEntrega) VALUES (%s, %s, %s, %s, %s)"

        values = (dataPedido, valorPedido, formaEntrega, statusEntrega, enderecoEntrega, cpfCliente)

        cursor.execute(sql, values)
        conexao.commit()

        print("Pedido online inserido")

        cursor.close()
        conexao.close()