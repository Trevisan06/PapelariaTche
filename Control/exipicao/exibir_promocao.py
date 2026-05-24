import mysql.connector
import sys
import os

# adiciona a pasta pai (Control) ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def exibir_dados_promocao():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM promocao")
        resultados = cursor.fetchall()

        print("\nPromoção:")

        for cod_promocao, nome, desconto, data_inicio, data_fim, motivo, cod_produto in resultados:
            print(f"Código: {cod_promocao} | Nome: {nome} | Desconto: {desconto} | Data início: {data_inicio} | Data fim: {data_fim} | Motivo: {motivo} | Código produto: {cod_produto}")

        cursor.close()
        conexao.close()