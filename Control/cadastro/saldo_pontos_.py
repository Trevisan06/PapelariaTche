import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_dados_saldo_pontos():
    conexao = conectar()

    if not conexao:
        print("Falha na conexão.")
        return

    try:
        cursor = conexao.cursor()

        idClientes               = input("CPF do cliente: ")
        saldoAtual               = int(input("Saldo atual: ") or "0")
        pontosGanhos             = int(input("Pontos ganhos: ") or "0")
        pontosUsados             = int(input("Pontos usados: ") or "0")
        dataDaUltimaMovimentacao = input("Data da última movimentação: ")
        statusDaConta            = input("Status da conta: ")

        sql = """
            INSERT INTO saldoPontos
                (idclientes, saldoAtual, pontosGanhos, pontosUsados, dataDaUltimaMovimentacao, statusDaconta)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (idClientes, saldoAtual, pontosGanhos, pontosUsados, dataDaUltimaMovimentacao, statusDaConta)

        cursor.execute(sql, values)
        conexao.commit()
        print("Saldo de pontos inserido com sucesso!")

    except Exception as e:
        conexao.rollback()
        print(f"Erro ao inserir saldo de pontos: {e}")

    finally:
        cursor.close()
        conexao.close()