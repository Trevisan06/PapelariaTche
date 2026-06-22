import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_dados_promocao():
    conexao = conectar()

    if not conexao:
        print("Falha na conexão.")
        return

    try:
        cursor = conexao.cursor()

        nome        = input("Nome da promoção: ")
        desconto    = int(input("Desconto: ") or "0")
        dataInicio  = input("Data de início: ")
        dataFim     = input("Data de fim: ")
        motivo      = input("Motivo: ")
        codProdutos = int(input("Código do produto: ") or "0")

        sql = """
            INSERT INTO promocao
                (nome, desconto, dataInicio, dataFim, motivo, codProdutos)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (nome, desconto, dataInicio, dataFim, motivo, codProdutos)

        cursor.execute(sql, values)
        conexao.commit()
        print("Promoção inserida com sucesso!")

    except Exception as e:
        conexao.rollback()
        print(f"Erro ao inserir promoção: {e}")

    finally:
        cursor.close()
        conexao.close()