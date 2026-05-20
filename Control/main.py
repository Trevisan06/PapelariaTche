from conexao import conectar

from clientes import inserir_dados_clientes
from categoria import inserir_dados_categoria
from filial import inserir_dados_filial
from funcionario import inserir_dados_funcionario
from produtos import inserir_dados_produtos
from compra import inserir_dados_compra
from pedido_online import inserir_dados_pedido_online
from parcelas import inserir_dados_parcelas
from saldo_pontos_ import inserir_dados_saldo_pontos
from promocao import inserir_dados_promocao

from exibir_clientes import exibir_dados_clientes
from exibir_categoria import exibir_dados_categoria
from exibir_filial import exibir_dados_filial
from exibir_funcionario import exibir_dados_funcionario
from exibir_produtos import exibir_dados_produtos
from exibir_compra import exibir_dados_compra
from exibir_pedido_online import exibir_dados_pedido_online
from exibir_parcelas import exibir_dados_parcelas
from exibir_saldo_pontos import exibir_dados_saldo_pontos
from exibir_promocao import exibir_dados_promocao


while True:
    conexao = conectar()

    print("\n===== PAPELARIA TCHE =====")
    print("1 - Clientes")
    print("2 - Categoria")
    print("3 - Filial")
    print("4 - Funcionário")
    print("5 - Produtos")
    print("6 - Compra")
    print("7 - Pedido Online")
    print("8 - Parcelas")
    print("9 - Saldo Pontos")
    print("10 - Promoção")
    print("0 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        print("\nClientes")
        inserir_dados_clientes()
        exibir_dados_clientes()

    elif opcao == "2":
        print("\nCategoria")
        inserir_dados_categoria()
        exibir_dados_categoria()

    elif opcao == "3":
        print("\nFilial")
        inserir_dados_filial()
        exibir_dados_filial()

    elif opcao == "4":
        print("\nFuncionário")
        inserir_dados_funcionario()
        exibir_dados_funcionario()

    elif opcao == "5":
        print("\nProdutos")
        inserir_dados_produtos()
        exibir_dados_produtos()

    elif opcao == "6":
        print("\nCompra")
        inserir_dados_compra()
        exibir_dados_compra()

    elif opcao == "7":
        print("\nPedido Online")
        inserir_dados_pedido_online()
        exibir_dados_pedido_online()

    elif opcao == "8":
        print("\nParcelas")
        inserir_dados_parcelas()
        exibir_dados_parcelas()

    elif opcao == "9":
        print("\nSaldo Pontos")
        inserir_dados_saldo_pontos()
        exibir_dados_saldo_pontos()

    elif opcao == "10":
        print("\nPromoção")
        inserir_dados_promocao()
        exibir_dados_promocao()

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")