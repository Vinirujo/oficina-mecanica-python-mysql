from conexao import conectar


def listar_clientes_veiculos():
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    SELECT clientes.nome, veiculos.modelo, veiculos.placa
    FROM clientes
    INNER JOIN veiculos
    ON clientes.id = veiculos.id_cliente
    """

    cursor.execute(sql)

    resultados = cursor.fetchall()

    if resultados:
        for resultado in resultados:
            print(resultado)
    else:
        print("Nenhum cliente com veículo cadastrado.")

    cursor.close()
    conexao.close()