import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_dados_pedido_online():
    conexao = conectar()

    if not conexao:
        print("Falha na conexão.")
        return

    try:
        cursor = conexao.cursor()

        dataPedido      = input("Data do pedido: ")
        valorPedido     = float(input("Valor do pedido: ") or "0")
        formaEntrega    = input("Forma de entrega: ")
        statusEntrega   = input("Status da entrega: ")
        enderecoEntrega = input("Endereço da entrega: ")
        cpf_cliente     = input("CPF do cliente: ")

        sql = """
            INSERT INTO pedidoOnline
                (dataPedido, valorPedido, formaEntrega, statusEntrega, enderecoEntrega, cpfCliente)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (dataPedido, valorPedido, formaEntrega, statusEntrega, enderecoEntrega, cpf_cliente)

        cursor.execute(sql, values)
        conexao.commit()
        print("Pedido online inserido com sucesso!")

    except Exception as e:
        conexao.rollback()
        print(f"Erro ao inserir pedido online: {e}")

    finally:
        cursor.close()
        conexao.close()