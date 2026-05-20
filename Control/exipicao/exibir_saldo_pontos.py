import mysql.connector
import sys
import os

# adiciona a pasta pai (Control) ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def exibir_dados_saldo_pontos():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM saldoPontos")
        resultados = cursor.fetchall()

        print("\nSaldo Pontos:")

        for id_pontos, cpf_cliente, saldo_atual, pontos_ganhos, pontos_usados, data_movimentacao, status_conta in resultados:
            print(f"ID: {id_pontos} | CPF Cliente: {cpf_cliente} | Saldo atual: {saldo_atual} | Pontos ganhos: {pontos_ganhos} | Pontos usados: {pontos_usados} | Última movimentação: {data_movimentacao} | Status conta: {status_conta}")

        cursor.close()
        conexao.close()