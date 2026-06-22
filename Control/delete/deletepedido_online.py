from conexao import conectar

def deletar_pedido_online(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM pedidoOnline WHERE id = %s", (id,))
    conexao.commit()

    if cursor.rowcount > 0:
        print(f"Pedido online com ID {id} deletado com sucesso!")
    else:
        print(f"Nenhum pedido online encontrado com o ID {id}.")

    cursor.close()
    conexao.close()

id = int(input("Digite o ID do pedido online a ser deletado: "))
deletar_pedido_online(id)