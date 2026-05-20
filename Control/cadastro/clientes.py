import mysql.connector
import sys
import os

# adiciona a pasta pai (Control) ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar

def inserir_dados_clientes():

    conexao = conectar()

    if conexao:
        cursor = conexao.cursor()

        cpf = int(input("CPF: "))
        nome = input("Nome: ")
        dataNascimento = input("Data de nascimento: ")
        pontos = int(input("Pontos: "))
        contato = int(input("Contato: "))
        email = input("Email: "
        dividas = input("dividas"))

        sql = "INSERT INTO clientes (cpf, nome, dataNascimento, pontos, contato, email) VALUES (%s, %s, %s, %s, %s, %s)"

        values = (cpf, nome, data_nascimento, pontos, contato, email)

        cursor.execute(sql, values)
        conexao.commit()

        print("Cliente inserido")

        cursor.close()
        conexao.close()