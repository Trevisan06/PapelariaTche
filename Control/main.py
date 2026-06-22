import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from conexao import conectar

from cadastro.clientes import inserir_dados_clientes
from cadastro.categoria import inserir_dados_categoria
from cadastro.filial import inserir_dados_filial
from cadastro.funcionario import inserir_dados_funcionario
from cadastro.produtos import inserir_dados_produtos
from cadastro.compra import inserir_dados_compra
from cadastro.pedido_online import inserir_dados_pedido_online
from cadastro.parcelas import inserir_dados_parcelas
from cadastro.saldo_pontos_ import inserir_dados_saldo_pontos
from cadastro.promocao import inserir_dados_promocao

from exipicao.exibir_clientes import exibir_dados_clientes
from exipicao.exibir_categoria import exibir_dados_categoria
from exipicao.exibir_filial import exibir_dados_filial
from exipicao.exibir_funcionario import exibir_dados_funcionario
from exipicao.exibir_produtos import exibir_dados_produtos
from exipicao.exibir_compra import exibir_dados_compra
from exipicao.exibir_pedido_online import exibir_dados_pedido_online
from exipicao.exibir_parcelas import exibir_dados_parcelas
from exipicao.exibir_saldo_pontos import exibir_dados_saldo_pontos
from exipicao.exibir_promocao import exibir_dados_promocao

from delete.deletecliente import deletar_cliente
from delete.deletecategoria import deletar_categoria
from delete.deletefilal import deletar_filial
from delete.deletefuncionario import deletar_funcionario
from delete.deleteprodutos import deletar_produto
from delete.deletecompra import deletar_compra
from delete.deletepedido_online import deletar_pedido_online
from delete.deleteparcelas import deletar_parcela
from delete.deletesaldo_pontos import deletar_saldo_pontos
from delete.deletepromocao import deletar_promocao

from view.fiado import exibir_fiado
from view.estabelecimento import exibir_estabelecimento
from view.corredor import exibir_corredor
from view.compraOnline import exibir_compra_online

while True:
    print("\n===== PAPELARIA TCHE =====")
    print("--- CADASTRO ---")
    print("1  - Cadastrar Cliente")
    print("2  - Cadastrar Categoria")
    print("3  - Cadastrar Filial")
    print("4  - Cadastrar Funcionário")
    print("5  - Cadastrar Produto")
    print("6  - Cadastrar Compra")
    print("7  - Cadastrar Pedido Online")
    print("8  - Cadastrar Parcelas")
    print("9  - Cadastrar Saldo Pontos")
    print("10 - Cadastrar Promoção")
    print("--- EXIBIR ---")
    print("11 - Exibir Clientes")
    print("12 - Exibir Categorias")
    print("13 - Exibir Filiais")
    print("14 - Exibir Funcionários")
    print("15 - Exibir Produtos")
    print("16 - Exibir Compras")
    print("17 - Exibir Pedidos Online")
    print("18 - Exibir Parcelas")
    print("19 - Exibir Saldo Pontos")
    print("20 - Exibir Promoções")
    print("--- DELETAR ---")
    print("21 - Deletar Cliente")
    print("22 - Deletar Categoria")
    print("23 - Deletar Filial")
    print("24 - Deletar Funcionário")
    print("25 - Deletar Produto")
    print("26 - Deletar Compra")
    print("27 - Deletar Pedido Online")
    print("28 - Deletar Parcela")
    print("29 - Deletar Saldo Pontos")
    print("30 - Deletar Promoção")
    print("--- VIEWS ---")
    print("31 - Exibir Fiado")
    print("32 - Exibir Estabelecimento")
    print("33 - Exibir Corredor")
    print("34 - Exibir Compra Online")
    print("0  - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        inserir_dados_clientes()
    elif opcao == "2":
        inserir_dados_categoria()
    elif opcao == "3":
        inserir_dados_filial()
    elif opcao == "4":
        inserir_dados_funcionario()
    elif opcao == "5":
        inserir_dados_produtos()
    elif opcao == "6":
        inserir_dados_compra()
    elif opcao == "7":
        inserir_dados_pedido_online()
    elif opcao == "8":
        inserir_dados_parcelas()
    elif opcao == "9":
        inserir_dados_saldo_pontos()
    elif opcao == "10":
        inserir_dados_promocao()
    elif opcao == "11":
        exibir_dados_clientes()
    elif opcao == "12":
        exibir_dados_categoria()
    elif opcao == "13":
        exibir_dados_filial()
    elif opcao == "14":
        exibir_dados_funcionario()
    elif opcao == "15":
        exibir_dados_produtos()
    elif opcao == "16":
        exibir_dados_compra()
    elif opcao == "17":
        exibir_dados_pedido_online()
    elif opcao == "18":
        exibir_dados_parcelas()
    elif opcao == "19":
        exibir_dados_saldo_pontos()
    elif opcao == "20":
        exibir_dados_promocao()
    elif opcao == "21":
        cpf = int(input("Digite o CPF do cliente a ser deletado: "))
        deletar_cliente(cpf)
    elif opcao == "22":
        id = int(input("Digite o ID da categoria a ser deletada: "))
        deletar_categoria(id)
    elif opcao == "23":
        id = int(input("Digite o ID da filial a ser deletada: "))
        deletar_filial(id)
    elif opcao == "24":
        id = int(input("Digite o ID do funcionário a ser deletado: "))
        deletar_funcionario(id)
    elif opcao == "25":
        id = int(input("Digite o código do produto a ser deletado: "))
        deletar_produto(id)
    elif opcao == "26":
        id = int(input("Digite o ID da compra a ser deletada: "))
        deletar_compra(id)
    elif opcao == "27":
        id = int(input("Digite o ID do pedido online a ser deletado: "))
        deletar_pedido_online(id)
    elif opcao == "28":
        id = int(input("Digite o código da parcela a ser deletada: "))
        deletar_parcela(id)
    elif opcao == "29":
        id = int(input("Digite o ID do saldo de pontos a ser deletado: "))
        deletar_saldo_pontos(id)
    elif opcao == "30":
        id = int(input("Digite o código da promoção a ser deletada: "))
        deletar_promocao(id)
    elif opcao == "31":
        exibir_fiado()
    elif opcao == "32":
        exibir_estabelecimento()
    elif opcao == "33":
        exibir_corredor()
    elif opcao == "34":
        exibir_compra_online()
    elif opcao == "0":
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida.")