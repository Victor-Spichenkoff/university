from program import *



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
def fill_list_real(lista: SimpleList):
    # 1:
    lista.inserirSemPrioridade(ListItem(Colors.Verde, lista.getLastCodeUsedByColor(Colors.Verde) + 1))
    lista.inserirComPrioridade(ListItem(Colors.Amarelo, lista.getLastCodeUsedByColor(Colors.Amarelo) + 1))
    lista.inserirComPrioridade(ListItem(Colors.Amarelo, lista.getLastCodeUsedByColor(Colors.Amarelo) + 1))
    # 4:
    lista.inserirComPrioridade(ListItem(Colors.Amarelo, lista.getLastCodeUsedByColor(Colors.Amarelo) + 1))(ListItem(Colors.Verde, lista.getLastCodeUsedByColor(Colors.Verde) + 1))
    lista.inserirSemPrioridade(ListItem(Colors.Verde, lista.getLastCodeUsedByColor(Colors.Verde) + 1))
    # 6:
    lista.inserirSemPrioridade(ListItem(Colors.Verde, lista.getLastCodeUsedByColor(Colors.Verde) + 1))
    lista.inserirComPrioridade(ListItem(Colors.Amarelo, lista.getLastCodeUsedByColor(Colors.Amarelo) + 1))
    # 8:
    lista.inserirSemPrioridade(ListItem(Colors.Verde, lista.getLastCodeUsedByColor(Colors.Verde) + 1))
    lista.inserirComPrioridade(ListItem(Colors.Amarelo, lista.getLastCodeUsedByColor(Colors.Amarelo) + 1))(ListItem(Colors.Verde, lista.getLastCodeUsedByColor(Colors.Verde) + 1))
    lista.inserirSemPrioridade(ListItem(Colors.Verde, lista.getLastCodeUsedByColor(Colors.Verde) + 1))
