from conexao import conectar

def deletar_filial(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM filial WHERE id = %s", (id,))
    conexao.commit()

    if cursor.rowcount > 0:
        print(f"Filial com ID {id} deletada com sucesso!")
    else:
        print(f"Nenhuma filial encontrada com o ID {id}.")

    cursor.close()
    conexao.close()


id = int(input("Digite o ID da filial a ser deletada: "))
deletar_filial(id)