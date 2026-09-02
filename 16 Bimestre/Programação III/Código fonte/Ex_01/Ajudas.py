import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')






""""
1  - V
2  - A
3  - A
4  - A
5  - V
6  - V
7  - A
8  - V
9  - A
10 - V

"""
def fill_list(lista):
    import program as p
    
    # 1:
    lista.inserirSemPrioridade(p.ListItem(p.Colors.Verde, lista.getLastCodeUsedByColor(p.Colors.Verde) + 1))
    lista.inserirComPrioridade(p.ListItem(p.Colors.Amarelo, lista.getLastCodeUsedByColor(p.Colors.Amarelo) + 1))
    lista.inserirComPrioridade(p.ListItem(p.Colors.Amarelo, lista.getLastCodeUsedByColor(p.Colors.Amarelo) + 1))
    # 4:
    lista.inserirComPrioridade(p.ListItem(p.Colors.Amarelo, lista.getLastCodeUsedByColor(p.Colors.Amarelo) + 1))
    lista.inserirSemPrioridade(p.ListItem(p.Colors.Verde, lista.getLastCodeUsedByColor(p.Colors.Verde) + 1))
    # 6:
    lista.inserirSemPrioridade(p.ListItem(p.Colors.Verde, lista.getLastCodeUsedByColor(p.Colors.Verde) + 1))
    lista.inserirComPrioridade(p.ListItem(p.Colors.Amarelo, lista.getLastCodeUsedByColor(p.Colors.Amarelo) + 1))
    # 8:
    lista.inserirSemPrioridade(p.ListItem(p.Colors.Verde, lista.getLastCodeUsedByColor(p.Colors.Verde) + 1))
    lista.inserirComPrioridade(p.ListItem(p.Colors.Amarelo, lista.getLastCodeUsedByColor(p.Colors.Amarelo) + 1))
    lista.inserirSemPrioridade(p.ListItem(p.Colors.Verde, lista.getLastCodeUsedByColor(p.Colors.Verde) + 1))
