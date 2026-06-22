from conexao import conectar

def deletar_saldo_pontos(idPontos):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM saldoPontos WHERE idPontos = %s", (idPontos,))
    conexao.commit()

    if cursor.rowcount > 0:
        print(f"Saldo de pontos com ID {idPontos} deletado com sucesso!")
    else:
        print(f"Nenhum saldo de pontos encontrado com o ID {idPontos}.")

    cursor.close()
    conexao.close()

idPontos = int(input("Digite o ID do saldo de pontos a ser deletado: "))
deletar_saldo_pontos(idPontos)