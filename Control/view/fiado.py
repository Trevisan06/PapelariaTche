import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def exibir_fiado():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM fiado")
        resultados = cursor.fetchall()

        print("\nFiado:")

        for idCompra, dataCompra, cpfCliente, codParcelas, valorParcela, statusParcela in resultados:
            print(f"ID Compra: {idCompra} | Data Compra: {dataCompra} | CPF Cliente: {cpfCliente} | Cód. Parcela: {codParcelas} | Valor Parcela: {valorParcela} | Status: {statusParcela}")

        cursor.close()
        conexao.close()