import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def exibir_dados_funcionario():
    conexao = conectar()

    if not conexao:
        print("Falha na conexão.")
        return

    try:
        cursor = conexao.cursor()

        cursor.execute("SELECT idFuncionarios, nome, cargo, telefone, matricula, metaDeVendas, idFilial FROM funcionario")
        resultados = cursor.fetchall()

        print("\nFuncionários:")

        for idFuncionarios, nome, cargo, telefone, matricula, metaDeVendas, idFilial in resultados:
            print(f"ID: {idFuncionarios} | Nome: {nome} | Cargo: {cargo} | Telefone: {telefone} | Matrícula: {matricula} | Meta de vendas: {metaDeVendas} | ID Filial: {idFilial}")

    except Exception as e:
        print(f"Erro ao exibir funcionários: {e}")

    finally:
        cursor.close()
        conexao.close()