print("")


# {var:-:^30}
def menu():
    print(f"{"Copyright Victor Spichenkoff Santana":-^65}")
    print((f"{"Cardápio":-^65}"))
    print(f"""{"-" * 65}
---| Tamanho  |   Pizza Salgada (PS)   |   Pizza  Doce(PD)   |---
---|    P     |        R$ 30.00        |       R$ 34.00      |---
---|    M     |        R$ 45.00        |       R$ 48.00      |---
---|    G     |        R$ 60.00        |       R$ 66.00      |---
{"-" * 65}""")


# Colcoar apenas "tamanho" ou "sabor"
def force_correct_value(label, valids):
    """
    :param label: "tamanho" ou "sabor"
    :param valids: array com os valores suportados, tudo em upper
    :return: valor correto
    """

    options_string = "/".join(valids)

    res = ""
    while True:
        res = input(f"Entre com o {label} desejado ({options_string}): ").upper()
        if not valids.__contains__(res):
            print(f"{label.title()} inválido. Tente novamente\n")
            continue

        break

    return res


# retorna o valor para a opção X de tamnho e y de sabor
# passar já verificado
def get_price(size, flavor):
    if flavor == "PS":
        if size == "P":
            return 30
        elif size == "M":
            return 45
        elif size == "G":
            return 60
    elif flavor == "PD":
        if size == "P":
            return 34
        elif size == "M":
            return 48
        elif size == "G":
            return 66
    else:
        print("Burlou a verificação. Só de castigo, vai pagar 100!!!")


def get_final_price():
    menu()
    final_price = 0

    while True:
        tamanho = force_correct_value("tamanho", ["P", "M", "G"])
        sabor = force_correct_value("sabor", ["PS", "PD"])
        current_value = get_price(tamanho, sabor)

        final_price += current_value

        more = input("Deseja mais alguma coisa: (S/N): ").upper()
        if more != "S":
            return final_price


final = get_final_price()
print(f"O valor final é de: R$ {final:0.2f}")
