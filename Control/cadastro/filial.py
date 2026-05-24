import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_dados_filial():
    conexao = conectar()

    if not conexao:
        print("Falha na conexão.")
        return

    try:
        cursor = conexao.cursor()

        nomeFilial             = input("Nome da filial: ")
        cidade                 = input("Cidade: ")
        estado                 = input("Estado: ")
        endereco               = input("Endereço: ")
        telefone               = input("Telefone: ")
        gerente                = input("Gerente: ")
        quantidadeFuncionarios = int(input("Quantidade de funcionários: ") or "0")
        horarioFuncionamento   = input("Horário de funcionamento: ")
        email                  = input("Email: ")

        sql = """
            INSERT INTO filial
                (nomeFilial, cidade, estado, endereco, telefone, gerente,
                 quantidadeFuncionarios, horarioFuncionamento, email)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (nomeFilial, cidade, estado, endereco, telefone, gerente,
                  quantidadeFuncionarios, horarioFuncionamento, email)

        cursor.execute(sql, values)
        conexao.commit()
        print("Filial inserida com sucesso!")

    except Exception as e:
        conexao.rollback()
        print(f"Erro ao inserir filial: {e}")

    finally:
        cursor.close()
        conexao.close()