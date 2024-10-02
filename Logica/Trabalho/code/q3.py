print("Copyright Victor Spichenkoff Santana")


# Area de pegar os valores
def escolha_tipo():
    """
    :return: o valor para o tipo x de madeira
    """
    chosen_type = ""

    while True:
        print("""Entre com o Tipo de Madeira desejado:
        PIN - Tora de Pinho 
        PER - Tora de Peroba 
        MOG - Tora de Mongno
        IPE - Tora de Ipê 
        IMB - Tora de Imbuia """)

        res = input(">>> ").upper()
        if res in ["PIN", "PER", "MOG", "IPE", "IMB"]:
            chosen_type = res
            break

        print("Tipo inválido. Tente novamente")

    price = 0
    match chosen_type:
        case "PIN":
            price = 150.40
        case "PER":
            price = 170.20
        case "MOG":
            price = 190.90
        case "IPE":
            price = 210.10
        case "IMB":
            price = 220.70

    return price


def qtd_toras():
    """
    :return: { "qtd": NUMBER, "discount_percent": [0, 0.16] }
    """
    qtd = -1
    percent_discount = 0
    while True:
        try:
            # Usei float, pois a unidade é m³
            res = float(input("Entre com a quantidade de toras (m³): "))

            if res <= 0:
                print("A quantidade deve ser maior que 0!")
            elif res > 2000:
                print("A quantidade máxima é de 2000m³!")
            else:
                qtd = res
                break
        except ValueError:
            print("Escreva um número válido")

    if qtd < 100:
        percent_discount = 0
    elif qtd < 500:
        percent_discount = 4/100
    elif qtd < 1000:
        percent_discount = 9/100
    elif qtd < 2000:
        percent_discount = 16/100

    return { "qtd": qtd, "discount_percent": percent_discount }


def transporte():
    print("""Escolha o tipo o tipo de Trasnporte
    1 - Trasporte Rodoviário - R$ 1000.00
    2 - Trasporte Ferroviário  - R$ 2000.00
    3 - Trasporte Hidroviário  - R$ 2500.00
    """)

    while True:
        res = input(">>> ")

        if res == "1":
            return 1000
        elif res == "2":
            return 2000
        elif res == "3":
            return 2500

        print("Trasporte inválido. Tente novamente")


# Trasformações
def give_discounted_price(original_price, qtd, discount_percent):
    """
    passar só se jpa estiver validado
    não conta o trasporte
    :param original_price: preço pegado pelo escolha_tipo
    :param qtd: qunatas unidades
    :param discount_percent: [0, 0.99] é quanto retira do original
    :return: o preço já descontado
    """

    return (original_price * qtd) * (1 - discount_percent)


# Execução
wood_price = escolha_tipo()
qtd_infos = qtd_toras()
trasp_price = transporte()


total_a_pagar = give_discounted_price(wood_price, qtd_infos["qtd"], qtd_infos["discount_percent"]) + trasp_price

print(f"O valor final é: {total_a_pagar}")
