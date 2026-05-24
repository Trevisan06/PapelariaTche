import mysql.connector
import sys
import os

# adiciona a pasta pai (Control) ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_dados_compra():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        dataCompra = input("Data da compra: ")
        valorCompra = float(input("Valor da compra: "))
        formaPagamento = input("Forma de pagamento: ")
        quantidadeItens = int(input("Quantidade de itens: "))
        codFornecedor = int(input("Código do produto: "))

        sql = "INSERT INTO compra (dataCompra, valorCompra, formaPagamento, quantidadeItens, codFornecedor) VALUES (%s, %s, %s, %s, %s, %s)"

        values = (dataCompra, valorCompra, formaPagamento, quantidadeItens, codFuncionario)

        cursor.execute(sql, values)
        conexao.commit()

        print("Compra inserida")

        cursor.close()
        conexao.close()