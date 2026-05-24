import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_dados_funcionario():
    conexao = conectar()

    if not conexao:
        print("Falha na conexão.")
        return

    try:
        cursor = conexao.cursor()

        idFuncionarios = int(input("ID do funcionário: ") or "0")
        nome           = input("Nome: ")
        cargo          = input("Cargo: ")
        salario        = float(input("Salário: ") or "0")
        telefone       = input("Telefone: ")
        matricula      = int(input("Matrícula: ") or "0")
        metaVendas     = input("Meta de vendas: ")
        idFilial       = int(input("ID da filial: ") or "0")

        sql = """
            INSERT INTO funcionario
                (idFuncionarios, nome, cargo, salario, telefone, matricula, metaDeVendas, idFilial)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (idFuncionarios, nome, cargo, salario, telefone, matricula, metaVendas, idFilial)

        cursor.execute(sql, values)
        conexao.commit()
        print("Funcionário inserido com sucesso!")

    except Exception as e:
        conexao.rollback()
        print(f"Erro ao inserir funcionário: {e}")

    finally:
        cursor.close()
        conexao.close()