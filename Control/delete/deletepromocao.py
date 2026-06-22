from conexao import conectar

def deletar_promocao(codPromocao):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM promocao WHERE codPromocao = %s", (codPromocao,))
    conexao.commit()

    if cursor.rowcount > 0:
        print(f"Promoção com código {codPromocao} deletada com sucesso!")
    else:
        print(f"Nenhuma promoção encontrada com o código {codPromocao}.")

    cursor.close()
    conexao.close()

codPromocao = int(input("Digite o código da promoção a ser deletada: "))
deletar_promocao(codPromocao)