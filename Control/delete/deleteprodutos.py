from conexao import conectar

def deletar_produto(codProduto):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM produtos WHERE codProduto = %s", (codProduto,))
    conexao.commit()

    if cursor.rowcount > 0:
        print(f"Produto com código {codProduto} deletado com sucesso!")
    else:
        print(f"Nenhum produto encontrado com o código {codProduto}.")

    cursor.close()
    conexao.close()

codProduto = int(input("Digite o código do produto a ser deletado: "))
deletar_produto(codProduto)