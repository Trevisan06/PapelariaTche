import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_dados_clientes():
    conexao = conectar()

    if not conexao:
        print("Falha na conexão.")
        return

    try:
        cursor = conexao.cursor()

        cpf            = input("CPF: ")
        nome           = input("Nome: ")
        dataNascimento = input("Data de nascimento: ")
        pontos         = int(input("Pontos: ") or "0")
        contato        = input("Contato: ")
        email          = input("Email: ")
        parcelas       = input("Parcelas: ")
        dividas        = input("Dívidas: ")

        sql = """
            INSERT INTO clientes
                (cpf, nome, dataNascimento, pontos, contato, email, parcelas, dividas)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (cpf, nome, dataNascimento, pontos, contato, email, parcelas, dividas)

        cursor.execute(sql, values)
        conexao.commit()
        print("Cliente inserido com sucesso!")

    except Exception as e:
        conexao.rollback()
        print(f"Erro ao inserir cliente: {e}")

    finally:
        cursor.close()
        conexao.close()
