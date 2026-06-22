import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def exibir_dados_clientes():
    conexao = conectar()

    if not conexao:
        print("Falha na conexão.")
        return

    try:
        cursor = conexao.cursor()

        cursor.execute("SELECT nome, contato, email FROM clientes")
        resultados = cursor.fetchall()

        print("\nClientes:")

        for nome, contato, email in resultados:
            print(f"Nome: {nome} | Contato: {contato} | Email: {email}")

    except Exception as e:
        print(f"Erro ao exibir clientes: {e}")

    finally:
        cursor.close()
        conexao.close()