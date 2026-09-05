import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')






""""
1  - V
2  - V
3  - V
4  - a
5  - a
6  - V
7  - v
8  - a
9  - a
10 - a

"""
def fill_list(lista):
    import program as p
    
    # 1:
    lista.inserirSemPrioridade(p.ListItem(p.Colors.Verde, lista.getLastCodeUsedByColor(p.Colors.Verde) + 1))
    lista.inserirSemPrioridade(p.ListItem(p.Colors.Verde, lista.getLastCodeUsedByColor(p.Colors.Verde) + 1))
    lista.inserirSemPrioridade(p.ListItem(p.Colors.Verde, lista.getLastCodeUsedByColor(p.Colors.Verde) + 1))
    # 4:
    lista.inserirComPrioridade(p.ListItem(p.Colors.Amarelo, lista.getLastCodeUsedByColor(p.Colors.Amarelo) + 1))
    lista.inserirComPrioridade(p.ListItem(p.Colors.Amarelo, lista.getLastCodeUsedByColor(p.Colors.Amarelo) + 1))
    # 6:
    lista.inserirSemPrioridade(p.ListItem(p.Colors.Verde, lista.getLastCodeUsedByColor(p.Colors.Verde) + 1))
    lista.inserirSemPrioridade(p.ListItem(p.Colors.Verde, lista.getLastCodeUsedByColor(p.Colors.Verde) + 1))
    # 8:
    lista.inserirComPrioridade(p.ListItem(p.Colors.Amarelo, lista.getLastCodeUsedByColor(p.Colors.Amarelo) + 1))
    lista.inserirComPrioridade(p.ListItem(p.Colors.Amarelo, lista.getLastCodeUsedByColor(p.Colors.Amarelo) + 1))
    lista.inserirComPrioridade(p.ListItem(p.Colors.Amarelo, lista.getLastCodeUsedByColor(p.Colors.Amarelo) + 1))
