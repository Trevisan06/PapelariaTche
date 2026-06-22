import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def exibir_dados_saldo_pontos():
    conexao = conectar()

    if not conexao:
        print("Falha na conexão.")
        return

    try:
        cursor = conexao.cursor()

        cursor.execute("SELECT idPontos, idclientes, saldoAtual, pontosGanhos, pontosUsados, dataDaUltimaMovimentacao, statusDaconta FROM saldoPontos")
        resultados = cursor.fetchall()

        print("\nSaldo de Pontos:")

        for idPontos, idclientes, saldoAtual, pontosGanhos, pontosUsados, dataDaUltimaMovimentacao, statusDaconta in resultados:
            print(f"ID: {idPontos} | Cliente: {idclientes} | Saldo: {saldoAtual} | Pontos ganhos: {pontosGanhos} | Pontos usados: {pontosUsados} | Última movimentação: {dataDaUltimaMovimentacao} | Status: {statusDaconta}")

    except Exception as e:
        print(f"Erro ao exibir saldo de pontos: {e}")

    finally:
        cursor.close()
        conexao.close()