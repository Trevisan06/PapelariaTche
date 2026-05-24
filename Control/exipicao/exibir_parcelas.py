import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def exibir_dados_parcelas():
    conexao = conectar()

    if not conexao:
        print("Falha na conexão.")
        return

    try:
        cursor = conexao.cursor()

        cursor.execute("SELECT codParcelas, codVenda, numeroParcela, valorParcela, dataVencimento, dataPagamento, statusParcela, idCompra FROM parcelas")
        resultados = cursor.fetchall()

        print("\nParcelas:")

        for codParcelas, codVenda, numeroParcela, valorParcela, dataVencimento, dataPagamento, statusParcela, idCompra in resultados:
            print(f"Código: {codParcelas} | Cód. Venda: {codVenda} | Número: {numeroParcela} | Valor: {valorParcela} | Vencimento: {dataVencimento} | Pagamento: {dataPagamento} | Status: {statusParcela} | ID Compra: {idCompra}")

    except Exception as e:
        print(f"Erro ao exibir parcelas: {e}")

    finally:
        cursor.close()
        conexao.close()