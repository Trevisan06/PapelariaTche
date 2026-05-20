import mysql.connector
import sys
import os

# adiciona a pasta pai (Control) ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_dados_saldo_pontos():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        idClientes = int(input("CPF do cliente: "))
        saldoAtual = int(input("Saldo atual: "))
        pontosGanhos = int(input("Pontos ganhos: "))
        pontosUsados = int(input("Pontos usados: "))
        dataDaUltimaMovimentacao = input("Data da última movimentação: ")
        stausDaConta = input("Status da conta: ")

        sql = "INSERT INTO saldoPontos (cpfCliente, saldoAtual, pontosGanhos, pontosUsados, dataDaUltimaMovimentacao, statusDaconta) VALUES (%s, %s, %s, %s, %s, %s)"

        values = (cpfCliente, saldoAtual, pontosGanhos, pontosUsados, dataDaUltimaMovimentacao, statusConta)

        cursor.execute(sql, values)
        conexao.commit()

        print("Saldo de pontos inserido")

        cursor.close()
        conexao.close()