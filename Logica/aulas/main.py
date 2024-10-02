from formatacao import *

# print(6 / 1.1)



print('\033[32;40m')

teste = [1]
if teste:
    print("è true")


palavra = "Eu sou o mior"

for letra in palavra:
    print(letra, end=", ")

print('')
# print(f"{red} Olá, Mundo! \033[")
print(change_color("red", "Olá, Mundo!"))
