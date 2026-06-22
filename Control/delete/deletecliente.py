from conexao import conectar

def deletar_cliente(cpf):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM clientes WHERE cpf = %s", (cpf,))
    conexao.commit()

    if cursor.rowcount > 0:
        print(f"Cliente com CPF {cpf} deletado com sucesso!")
    else:
        print(f"Nenhum cliente encontrado com o CPF {cpf}.")

    cursor.close()
    conexao.close()

cpf = int(input("Digite o CPF do cliente a ser deletado: "))
deletar_cliente(cpf)