import mysql.connector
import sys
import os

# adiciona a pasta pai (Control) ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def exibir_dados_funcionario():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT id_funcionario, nome, cargo,telefone, matricula, meta_vendas, id_filial FROM funcionario")
        resultados = cursor.fetchall()

        print("\nFuncionário:")

        for id_funcionario, nome, cargo,telefone, matricula, meta_vendas, id_filial in resultados:
            print(f"ID: {id_funcionario} | Nome: {nome} | Cargo: {cargo} |Telefone: {telefone} | Matrícula: {matricula} | Meta de vendas: {meta_vendas} | ID Filial: {id_filial}")

        cursor.close()
        conexao.close()
