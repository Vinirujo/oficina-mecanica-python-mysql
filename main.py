from clientes import(
    cadastrar_cliente,
    listar_clientes,
    atualizar_cliente,
    excluir_cliente
)

from veiculos import(
    cadastrar_veiculo,
    listar_veiculos,
    atualizar_veiculo,
    excluir_veiculo
)

from consultas import (listar_clientes_veiculos)


while True:
    print("\n===== OFICINA MECÂNICA =====")
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Atualizar cliente")
    print("4 - Excluir cliente")
    print("5 - Cadastrar veículo")
    print("6 - Listar veículos")
    print("7 - Atualizar veículo")
    print("8 - Excluir veículo")
    print("9 - Listar clientes e veículos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente()

    elif opcao == "2":
        listar_clientes()

    elif opcao == "3":
        atualizar_cliente()

    elif opcao == "4":
        excluir_cliente()

    elif opcao == "5":
        cadastrar_veiculo()

    elif opcao == "6":
        listar_veiculos()

    elif opcao == "7":
        atualizar_veiculo()

    elif opcao == "8":
        excluir_veiculo()

    elif opcao == "9":
        listar_clientes_veiculos()

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")