from conexao import conectar

def deletar_categoria(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM categoria WHERE id = %s", (id,))
    conexao.commit()

    if cursor.rowcount > 0:
        print(f"Categoria com ID {id} deletada com sucesso!")
    else:
        print(f"Nenhuma categoria encontrada com o ID {id}.")

    cursor.close()
    conexao.close()


id = int(input("Digite o ID da categoria a ser deletada: "))
deletar_categoria(id)