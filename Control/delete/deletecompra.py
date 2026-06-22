from conexao import conectar

def deletar_compra(idCompra):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM compra WHERE idCompra = %s", (idCompra,))
    conexao.commit()

    if cursor.rowcount > 0:
        print(f"Compra com ID {idCompra} deletada com sucesso!")
    else:
        print(f"Nenhuma compra encontrada com o ID {idCompra}.")

    cursor.close()
    conexao.close()


idCompra = int(input("Digite o ID da compra a ser deletada: "))
deletar_compra(idCompra)