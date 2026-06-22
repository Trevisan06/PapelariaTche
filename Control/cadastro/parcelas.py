import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_dados_parcelas():
    conexao = conectar()

    if not conexao:
        print("Falha na conexão.")
        return

    try:
        cursor = conexao.cursor()

        numeroParcela  = int(input("Número da parcela: ") or "0")
        valorParcela   = float(input("Valor da parcela: ") or "0")
        dataVencimento = input("Data de vencimento: ")
        dataPagamento  = input("Data de pagamento: ")
        statusParcela  = input("Status da parcela: ")

        sql = """
            INSERT INTO parcelas
                (numeroParcela, valorParcela, dataVencimento, dataPagamento, statusParcela)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (numeroParcela, valorParcela, dataVencimento, dataPagamento, statusParcela)

        cursor.execute(sql, values)
        conexao.commit()
        print("Parcela inserida com sucesso!")

    except Exception as e:
        conexao.rollback()
        print(f"Erro ao inserir parcela: {e}")

    finally:
        cursor.close()
        conexao.close()