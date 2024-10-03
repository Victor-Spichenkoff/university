print("Copyright Victor Spichenkoff Santana\n")

"""
Estrutura = [
    {
        id: global ++,
        
    }
]"""
lista_contatos = []
id_global = 4767042
original_global_id = id_global

# Para testar:
id_global += 1
eu = {'id': id_global, 'nome': 'Victor', 'atividade': 'Piloto de F1', 'telefone': '902372307'}
lista_contatos.append(eu)


# Menus:
def main_menu():
    """
    :return: [1, 4], a opçção escolhida
    """
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
                return res
        except ValueError:
            print("Errado, tente novamente!")

        print("Errado, tente novamente!")


def consult_menu():
    """
    :return: [1, 4], a opçção escolhida
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

        print("Opção inválida, tente novamente!")


def cadastrar_contato(_id):
    nome = input("Por favor, entre com o NOME do contato: ")
    atividade = input("Por favor, entre com o ATIVIDADE do contato: ")
    tel = input("Por favor, entre com o TELEFONE do contato: ")

    obj = {
        "id": _id,
        "nome": nome,
        "atividade": atividade,
        "telefone": tel
    }

    lista_contatos.append(obj)


# Consulta
# # Utils - pegam dados e printam, cuidam de tudo para cada tipo, só chamar
def get_all():
    for contact in lista_contatos:
        print(f"ID        -->  {contact["id"]}")
        print(f"Nome      -->  {contact["nome"]}")
        print(f"Atividade -->  {contact["atividade"]}")
        print(f"Telefone  -->  {contact["telefone"]}\n")

    print("-" * 28 + "\n\n")


def get_by_id():
    """
    * Se tiver, printa, senão, avisa que não exoste
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
    for contact in lista_contatos:
        if contact["id"] == _id:
            print(f"{"-" * 28}")
            print(f"ID        -->  {contact["id"]}")
            print(f"Nome      -->  {contact["nome"]}")
            print(f"Atividade -->  {contact["atividade"]}")
            print(f"Telefone  -->  {contact["telefone"]}")
            print(f"\n{"-" * 28} \n")

    print(f"Nenhum contato encontrado com ID: {_id}")


# Consulta em si
def consultar_contatos():
    while True:
        option = consult_menu()

        match option:
            case 1:
                get_all()
            case 2:
                get_by_id()
            case 4:
                return


while True:
    main_option = main_menu()

    match main_option:
        case 1:
            id_global += 1
            cadastrar_contato(id_global)
        case 2:
            consultar_contatos()
        case 3:
            ""
        case 4:
            print("Até mais 👋")
            break

# print(lista_contatos)
