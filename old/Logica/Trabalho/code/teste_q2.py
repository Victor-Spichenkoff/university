def menu():
    print(f"{"Copyright Victor Spichenkoff Santana":-^65}")
    print((f"{"Cardápio":-^65}"))
    print(f"""{"-" * 65}  
---| Tamanho  |   Pizza Salgada (PS)   |   Pizza  Doce(PD)   |---  
---|    P     |        R$ 30.00        |       R$ 34.00      |---  
---|    M     |        R$ 45.00        |       R$ 48.00      |---  
---|    G     |        R$ 60.00        |       R$ 66.00      |---  
{"-" * 65}""")


# Colocar apenas "tamanho" ou "sabor"
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
        if res not in valids:
            # Print com o respectivo titulo apropriado
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
        return 100

        # Converte a abreviação para um texto.


def get_pizza_label(abrev):
    """
    :param abrev: ou PS ou PD
    :return: O nome pizza + o tipo
    """
    if abrev == "PS":
        return "Pizza Salgada"
    elif abrev == "PD":
        return "Pizza Doce"


def get_final_price():
    menu()

    # acumulador:
    final_price = 0

    while True:
        # Inputs:
        sabor = force_correct_value("sabor", ["PS", "PD"])
        tamanho = force_correct_value("tamanho", ["P", "M", "G"])
        # Pegar o preço:
        current_price = get_price(tamanho, sabor)

        final_price += current_price

        pizza_name = get_pizza_label(sabor)
        print(f"Você pediu uma {pizza_name} no tamanho {tamanho}: R$ {current_price}\n")

        more = input("Deseja mais alguma coisa: (S/N): ").upper()
        if more != "S":
            return final_price


final = get_final_price()
print(f"\nO valor total a ser pago: R$ {final:0.2f}")
