import mysql.connector
import sys
import os

# adiciona a pasta pai (Control) ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_dados_filial():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        nomeFilial = input("Nome da filial: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        endereco = input("Endereço: ")
        telefone = int(input("Telefone: "))
        gerente = input("Gerente: ")
        quantidadeFuncionarios = int(input("Quantidade de funcionários: "))
        horarioFuncionamento = input("Horário de funcionamento: ")
        email = input("Email: ")
        cpf_cliente = int(input("CPF do cliente: "))

        sql = "INSERT INTO filial (nomeFilial, cidade, estado, endereco, telefone, gerente, quantidadeFuncionarios, horarioFuncionamento, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        values = (nomeFilial, cidade, estado, endereco, telefone, gerente, quantidadeFuncionarios, horarioFuncionamento, email)

        cursor.execute(sql, values)
        conexao.commit()

        print("Filial inserida")

        cursor.close()
        conexao.close()
