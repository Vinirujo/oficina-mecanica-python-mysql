from conexao import conectar


def cadastrar_cliente():
    conexao = conectar()
    cursor = conexao.cursor()
    
    nome = input("Digite o nome do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    
    sql = """
    INSERT INTO clientes(nome, telefone)
    VALUES (%s, %s)
    """
    dados = (nome, telefone)
    
    cursor.execute(sql, dados)
    conexao.commit()
    
    print("Cliente cadastrado com sucesso")
    
    cursor.close()
    conexao.close()
    
def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute ("SELECT * FROM clientes")
    
    resultados = cursor.fetchall()
    
    if resultados:
        for cliente in resultados:
            print(cliente)
    else:
        print("Nenhum cliente cadastrado.")

    cursor.close()
    conexao.close()
    
def atualizar_cliente():
    conexao = conectar()
    cursor = conexao.cursor()

    id_cliente = int(input("Digite o ID do cliente: "))
    novo_telefone = input("Digite o novo telefone: ")

    sql = """
    UPDATE clientes
    SET telefone = %s
    WHERE id = %s
    """

    dados = (novo_telefone, id_cliente)

    cursor.execute(sql, dados)
    conexao.commit()

    if cursor.rowcount > 0:
        print("Cliente atualizado com sucesso!")
    else:
        print("Nenhum cliente encontrado com esse ID.")

    cursor.close()
    conexao.close()
    
def excluir_cliente():
    conexao = conectar()
    cursor = conexao.cursor()

    id_cliente = int(input("Digite o ID do cliente que deseja excluir: "))

    confirmacao = input(
        "Tem certeza que deseja excluir este cliente? (S/N): "
    ).upper()

    if confirmacao == "S":
        sql = """
        DELETE FROM clientes
        WHERE id = %s
        """

        dados = (id_cliente,)

        cursor.execute(sql, dados)
        conexao.commit()

        if cursor.rowcount > 0:
            print("Cliente excluído com sucesso!")
        else:
            print("Nenhum cliente encontrado com esse ID.")
    else:
        print("Exclusão cancelada.")

    cursor.close()
    conexao.close()