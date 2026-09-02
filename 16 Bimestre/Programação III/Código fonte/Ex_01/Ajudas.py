import os
import ajuda2 as a


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def fill_list(lista):
    a.fill_list_real(lista)
