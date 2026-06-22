from conexao import conectar

def deletar_parcela(codParcelas):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM parcelas WHERE codParcelas = %s", (codParcelas,))
    conexao.commit()

    if cursor.rowcount > 0:
        print(f"Parcela com código {codParcelas} deletada com sucesso!")
    else:
        print(f"Nenhuma parcela encontrada com o código {codParcelas}.")

    cursor.close()
    conexao.close()

codParcelas = int(input("Digite o código da parcela a ser deletada: "))
deletar_parcela(codParcelas)