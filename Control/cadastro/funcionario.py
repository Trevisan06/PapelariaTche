import mysql.connector
import sys
import os

# adiciona a pasta pai (Control) ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_dados_funcionario():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        nome = input("Nome: ")
        cargo = input("Cargo: ")
        salario = float(input("Salário: "))
        telefone = int(input("Telefone: "))
        matricula = int(input("Matrícula: "))
        metaVendas = input("Meta de vendas: ")
        idFilial = int(input("ID da filial: "))

        sql = "INSERT INTO funcionario (nome, cargo, salario, telefone, matricula, metaDeVendas, idFilial) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        values = (nome, cargo, salario, telefone, matricula, meta_vendas, id_filial)

        cursor.execute(sql, values)
        conexao.commit()

        print("Funcionário inserido")

        cursor.close()
        conexao.close()