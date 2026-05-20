import mysql.connector
import sys
import os

# adiciona a pasta pai (Control) ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def exibir_dados_filial():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT id_filial, nome_filial, cidade, estado, telefone, gerente, quantidade_funcionarios, horario_funcionamento, email FROM filial")
        resultados = cursor.fetchall()

        print("\nFilial:")

        for id_filial, nome_filial, cidade, estado, telefone, gerente, quantidade_funcionarios, horario_funcionamento, email in resultados:
            print(f"ID: {id_filial} | Nome: {nome_filial} | Cidade: {cidade} | Estado: {estado} |  Telefone: {telefone} | Gerente: {gerente} | Funcionários: {quantidade_funcionarios} | Horário: {horario_funcionamento} | Email: {email} |

        cursor.close()
        conexao.close()
