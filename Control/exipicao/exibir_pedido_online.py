import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def exibir_dados_pedido_online():
    conexao = conectar()

    if not conexao:
        print("Falha na conexão.")
        return

    try:
        cursor = conexao.cursor()

        cursor.execute("SELECT id, dataPedido, valorPedido, formaEntrega, statusEntrega, enderecoEntrega, cpfCliente FROM pedidoOnline")
        resultados = cursor.fetchall()

        print("\nPedidos Online:")

        for id, dataPedido, valorPedido, formaEntrega, statusEntrega, enderecoEntrega, cpfCliente in resultados:
            print(f"ID: {id} | Data: {dataPedido} | Valor: {valorPedido} | Forma entrega: {formaEntrega} | Status: {statusEntrega} | Endereço: {enderecoEntrega} | CPF Cliente: {cpfCliente}")

    except Exception as e:
        print(f"Erro ao exibir pedidos online: {e}")

    finally:
        cursor.close()
        conexao.close()