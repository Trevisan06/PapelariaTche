import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def exibir_dados_filial():
    conexao = conectar()

    if not conexao:
        print("Falha na conexão.")
        return

    try:
        cursor = conexao.cursor()

        cursor.execute("SELECT id, nomeFilial, cidade, estado, telefone, gerente, quantidadeFuncionarios, horarioFuncionamento, email FROM filial")
        resultados = cursor.fetchall()

        print("\nFiliais:")

        for id, nomeFilial, cidade, estado, telefone, gerente, quantidadeFuncionarios, horarioFuncionamento, email in resultados:
            print(f"ID: {id} | Nome: {nomeFilial} | Cidade: {cidade} | Estado: {estado} | Telefone: {telefone} | Gerente: {gerente} | Funcionários: {quantidadeFuncionarios} | Horário: {horarioFuncionamento} | Email: {email}")

    except Exception as e:
        print(f"Erro ao exibir filiais: {e}")

    finally:
        cursor.close()
        conexao.close()