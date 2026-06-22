import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def exibir_corredor():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM corredor")
        resultados = cursor.fetchall()

        print("\nCorredor:")

        for codProduto, nome, preco, quantidadeEstoque, id, nomeCategoria, setor in resultados:
            print(f"Cód. Produto: {codProduto} | Nome: {nome} | Preço: {preco} | Estoque: {quantidadeEstoque} | ID Categoria: {id} | Categoria: {nomeCategoria} | Setor: {setor}")

        cursor.close()
        conexao.close()