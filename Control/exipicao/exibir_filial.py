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

        cursor.execute("SELECT * FROM filial")
        resultados = cursor.fetchall()

        print("\nFilial:")

        for id_filial, nome_filial, cidade, estado, endereco, telefone, gerente, quantidade_funcionarios, horario_funcionamento, email, cpf_cliente in resultados:
            print(f"ID: {id_filial} | Nome: {nome_filial} | Cidade: {cidade} | Estado: {estado} | Endereço: {endereco} | Telefone: {telefone} | Gerente: {gerente} | Funcionários: {quantidade_funcionarios} | Horário: {horario_funcionamento} | Email: {email} | CPF Cliente: {cpf_cliente}")

        cursor.close()
        conexao.close()