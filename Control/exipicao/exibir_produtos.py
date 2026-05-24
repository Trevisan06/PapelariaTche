import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def exibir_dados_produtos():
    conexao = conectar()

    if not conexao:
        print("Falha na conexão.")
        return

    try:
        cursor = conexao.cursor()

        cursor.execute("SELECT codProduto, nome, categoria, preco, quantidadeEstoque, marca, validade, idCategoria FROM produtos")
        resultados = cursor.fetchall()

        print("\nProdutos:")

        for codProduto, nome, categoria, preco, quantidadeEstoque, marca, validade, idCategoria in resultados:
            print(f"Código: {codProduto} | Nome: {nome} | Categoria: {categoria} | Preço: {preco} | Estoque: {quantidadeEstoque} | Marca: {marca} | Validade: {validade} | ID Categoria: {idCategoria}")

    except Exception as e:
        print(f"Erro ao exibir produtos: {e}")

    finally:
        cursor.close()
        conexao.close()