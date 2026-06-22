import mysql.connector
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def exibir_estabelecimento():
    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM estabelecimento")
        resultados = cursor.fetchall()

        print("\nEstabelecimento:")

        for id, nomeFilial, horarioFuncionamento, idFuncionarios, nome, cargo in resultados:
            print(f"ID Filial: {id} | Filial: {nomeFilial} | Horário: {horarioFuncionamento} | ID Funcionário: {idFuncionarios} | Nome: {nome} | Cargo: {cargo}")

        cursor.close()
        conexao.close()