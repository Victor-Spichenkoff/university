import os


# Criar uma função de formatar titulos variáves

def titulo(label):
    size = len(label)
    print("* " + "-" * size + " *")
    print("| " + label + " |")
    print("* " + "-" * size + " *")


titulo("Titulo original")
print()
titulo("Nhe")


# Função dentro de função com parametros
def pai():
    var = "Nhe"
    filho(var)
    print("No pai ao final: " + var)


def filho(var):
    var = "Fome"
    print("No filho:" + var)


pai()


# Docstring
def soma(n1, n2):
    """
    :param n1: número 1
    :param n2: número
    :return: soma deles
    """
    return n1 + n2


print(soma(2, 4))


# Challenges
def factorial(x):
    result = 1
    # for n in range(x, 0, -1):
    #     result *= n

    while x > 0:
        result *= x
        x -= 1

    return result


print(factorial(6))


# -----------------
# FILES
# -----------------

def file_exists(name):
    try:
        file = open(name, "rt")
        file.close()
        return True
    except FileNotFoundError:

        return False


def create_file(name):
    try:
        file = open(name, "wt+")
        file.close()

        print("Criado em: " + name)
    except:
        print("Erro ao criar arquivo")


file_name = "store.txt"

if file_exists(file_name):
    print("Exite!")
else:
    create_file(file_name)


def add_to_file():
    text = input("O que adicionar: ")
    try:
        file = open(file_name, "at")
        with open(file_name, "at") as file:
            file.write(text + "\n")
    except:
        print("Erro ao editar")


add_to_file()

with open(file_name, "rt+") as file:
    print(file.read())
