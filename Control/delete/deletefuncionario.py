from conexao import conectar

def deletar_funcionario(idFuncionarios):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM funcionario WHERE idFuncionarios = %s", (idFuncionarios,))
    conexao.commit()

    if cursor.rowcount > 0:
        print(f"Funcionário com ID {idFuncionarios} deletado com sucesso!")
    else:
        print(f"Nenhum funcionário encontrado com o ID {idFuncionarios}.")

    cursor.close()
    conexao.close()

idFuncionarios = int(input("Digite o ID do funcionário a ser deletado: "))
deletar_funcionario(idFuncionarios)