print("Copyright Victor Spichenkoff Santana")


# valor base e idade, decide porcentagem de acrescimo e aumenta o valor conforme ele
# Retonar -1 em caso de entrada errada
def give_increased(base, age):
    percent = 1
    if base < 0 or age < 0:
        return -1
    # são validos. escolher a porcentagem
    elif age < 19:
        percent = 1
    elif age < 29:
        percent = 1.5
    elif age < 39:
        percent = 2.25
    elif age < 49:
        percent = 2.4
    elif age < 59:
        percent = 3.5
    else:
        percent = 6

    return base * percent


# Pegar os valores
valorBase = float(input("Qual o valor base: "))
idade = int(input("Qual a idade: "))

# Converter e exibir
valorMensal = give_increased(valorBase, idade)
if valorMensal == -1:
    print("Entrada(s) inválida(s)")
else:
    print(f"O valor mensal do plano é: R$ {valorMensal:.2f}")
