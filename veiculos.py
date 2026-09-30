from conexao import conectar


def cadastrar_veiculo():
    conexao = conectar()
    cursor = conexao.cursor()

    modelo = input("Digite o modelo do veículo: ")
    placa = input("Digite a placa do veículo: ")
    id_cliente = int(input("Digite o ID do cliente dono do veículo: "))

    sql = """
    INSERT INTO veiculos (modelo, placa, id_cliente)
    VALUES (%s, %s, %s)
    """

    dados = (modelo, placa, id_cliente)

    cursor.execute(sql, dados)
    conexao.commit()

    print("Veículo cadastrado com sucesso!")

    cursor.close()
    conexao.close()
    
def listar_veiculos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM veiculos")

    resultados = cursor.fetchall()

    if resultados:
        for veiculo in resultados:
            print(veiculo)
    else:
        print("Nenhum veículo cadastrado.")

    cursor.close()
    conexao.close()

def atualizar_veiculo():
    conexao = conectar()
    cursor = conexao.cursor()

    id_veiculo = int(input("Digite o ID do veículo: "))
    nova_placa = input("Digite a nova placa: ")

    sql = """
    UPDATE veiculos
    SET placa = %s
    WHERE id_veiculo = %s
    """

    dados = (nova_placa, id_veiculo)

    cursor.execute(sql, dados)
    conexao.commit()

    if cursor.rowcount > 0:
        print("Veículo atualizado com sucesso!")
    else:
        print("Nenhum veículo encontrado com esse ID.")

    cursor.close()
    conexao.close()

def excluir_veiculo():
    conexao = conectar()
    cursor = conexao.cursor()

    id_veiculo = int(input("Digite o ID do veículo que deseja excluir: "))

    confirmacao = input(
        "Tem certeza que deseja excluir este veículo? (S/N): "
    ).upper()

    if confirmacao == "S":
        sql = """
        DELETE FROM veiculos
        WHERE id_veiculo = %s
        """

        dados = (id_veiculo,)

        cursor.execute(sql, dados)
        conexao.commit()

        if cursor.rowcount > 0:
            print("Veículo excluído com sucesso!")
        else:
            print("Nenhum veículo encontrado com esse ID.")
    else:
        print("Exclusão cancelada.")

    cursor.close()
    conexao.close()