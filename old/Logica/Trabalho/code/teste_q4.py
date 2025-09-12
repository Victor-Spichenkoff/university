print("Copyright Victor Spichenkoff Santana\n")

lista_contatos = []
id_global = 4767042
original_global_id = id_global


# Menus:

def consult_menu():
    """
    :return: [1, 4], a opção escolhida
    """

    print("-" * 50)
    print(f"{"MENU CONSULTAR CONTATOS":-^50}")
    print("""Escolha a opção desejada: 
    1 - Consultar TODOS os contatos  
    2 - Consultar contato por ID 
    3 - Consultar contato(s) por ATIVIDADE 
    4 - Retornar """)
    while True:
        try:
            res = int(input(">>> "))
            if 1 <= res <= 4:
                print("-" * 28)
                return res
        except ValueError:
            print("Errado, tente novamente!")
            continue

        print("Opção inválida, tente novamente!")

    # Cadastro - Ele cuida de tudo, menos pegar o id


def cadastrar_contato(_id):
    nome = input("Por favor, entre com o NOME do contato: ")
    atividade = input("Por favor, entre com o ATIVIDADE do contato: ")
    tel = input("Por favor, entre com o TELEFONE do contato: ")

    contact_obj = {
        "id": _id,
        "nome": nome,
        "atividade": atividade,
        "telefone": tel
    }

    lista_contatos.append(contact_obj.copy())


# Consulta
# # Utils - pegam dados e printam, cuidam de tudo para cada tipo, só chamar
def get_all():
    if len(lista_contatos) < 1:
        print(f"{'Sem Contatos': ^28}")
        return print("-" * 28 + "\n\n")

    for contact in lista_contatos:
        print(f"ID        -->  {contact["id"]}")
        print(f"Nome      -->  {contact["nome"]}")
        print(f"Atividade -->  {contact["atividade"]}")
        print(f"Telefone  -->  {contact["telefone"]}\n")

    print("-" * 28 + "\n\n")


def get_by_id():
    """
    * Se tiver, printa, senão, avisa que não existe
    :return: void
    """
    _id = 0

    while True:
        try:
            _id = int(input("Qual o ID (menor é 4767043): "))

            if _id > original_global_id:
                break
        except ValueError:
            print("Digite um número!")

        print(f"Digite um número maior que {original_global_id}")

        # pegar por id
    print(f"\n{"-" * 28}")
    for contact in lista_contatos:
        if contact["id"] == _id:
            print(f"ID        -->  {contact["id"]}")
            print(f"Nome      -->  {contact["nome"]}")
            print(f"Atividade -->  {contact["atividade"]}")
            print(f"Telefone  -->  {contact["telefone"]}")
            print(f"\n{"-" * 28} \n")

            return

    print(f"Nenhum contato encontrado com ID: {_id}")
    print(f"{"-" * 28} \n")


def get_by_activity():
    """
    Consegue pegar por aproximação. Ex:
    - pilot -> Piloto de F1
    :return: void
    """
    activity = input("Digite a  ATIVIDADE do(s) contato(s): ").lower()

    query_result = []
    for contact in lista_contatos:
        if activity in contact["atividade"].lower():
            query_result.append(contact)

    print(f"{"-" * 28}")
    if len(query_result):
        for filtered_contact in query_result:
            print(f"ID        -->  {filtered_contact["id"]}")
            print(f"Nome      -->  {filtered_contact["nome"]}")
            print(f"Atividade -->  {filtered_contact["atividade"]}")
            print(f"Telefone  -->  {filtered_contact["telefone"]}\n")

        return print(f"{"-" * 28} \n")

    print("Nenhum contato encontrado com Atividade: " + activity.upper())
    print(f"{"-" * 28} \n")


# Consulta em si
def consultar_contatos():
    while True:
        option = consult_menu()

        match option:
            case 1:
                get_all()
            case 2:
                get_by_id()
            case 3:
                get_by_activity()
            case 4:
                return

            # Remoção - Só ele cuida de tudo


def remover_contato():
    # Sair se não tive contato, evitar loop infinito. Sim, eu cai nele
    if not len(lista_contatos):
        print("\n" + "-" * 28)
        print("Sem contato para apagar")
        return print("-" * 28 + "\n")

    while True:
        try:
            _id = int(input(f"Qual o ID que vai ser removido (começa em {original_global_id + 1}): "))

            print("\n" + "-" * 28)
            # No range, começa em 0 e o ultimo não é considerado
            for i in range(len(lista_contatos)):
                if lista_contatos[i]["id"] == _id:
                    del lista_contatos[i]

                    print("Contato apagado")
                    return print("-" * 28 + "\n")

            print(f"{f'ID inválido: {_id}': ^28}")
            print("-" * 28 + "\n")
        except ValueError:
            print("ID inválido!")

        # Execução


while True:
    main_option = ""

    # Menu principal
    print("-" * 50)
    print(f"{"MENU PRINCIPAL":-^50}")
    print("""Escolha a opção desejada: 
        1 - Cadastrar Contato    
        2 - Consultar Contato(s) 
        3 - Remover Contato 
        4 - Sair """)
    while True:
        try:
            res = int(input(">>> "))
            if 1 <= res <= 4:
                main_option = res
                break
        except ValueError:
            print("Errado, tente novamente!")
            continue

        print("Errado, tente novamente!")

        # O que fazer
    match main_option:
        case 1:
            id_global += 1
            cadastrar_contato(id_global)
        case 2:
            consultar_contatos()
        case 3:
            remover_contato()
        case 4:
            print("Até mais 👋")
