import mysql.connector
import sys
import os

# adiciona a pasta pai (Control) ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def exibir_dados_produtos():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM produtos")
        resultados = cursor.fetchall()

        print("\nProdutos:")

        for cod_produto, nome, preco, quantidade_estoque, marca, validade, id_categoria in resultados:
            print(f"Código: {cod_produto} | Nome: {nome} | Preço: {preco} | Estoque: {quantidade_estoque} | Marca: {marca} | Validade: {validade} | ID Categoria: {id_categoria}")

        cursor.close()
        conexao.close()