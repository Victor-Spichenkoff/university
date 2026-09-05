from program import *




lista = LinkedList()




lista.inserirComPrioridade(ListItem(Colors.Verde, 202))
lista.inserirSemPrioridade(ListItem("A", 4))
lista.inserirSemPrioridade(ListItem(Colors.Verde, lista.getLastCodeUsedByColor(Colors.Verde) + 1))
lista.inserirSemPrioridade(ListItem(Colors.Verde, lista.getLastCodeUsedByColor(Colors.Verde) + 1))
lista.inserirComPrioridade(ListItem(Colors.Verde, lista.getLastCodeUsedByColor(Colors.Amarelo) + 1))
lista.inserirSemPrioridade(ListItem(Colors.Verde, lista.getLastCodeUsedByColor(Colors.Verde) + 1))
lista.inserirComPrioridade(ListItem(Colors.Verde, lista.getLastCodeUsedByColor(Colors.Amarelo) + 1))
lista.inserirComPrioridade(ListItem(Colors.Verde, lista.getLastCodeUsedByColor(Colors.Amarelo) + 1))
lista.inserirSemPrioridade(ListItem(Colors.Verde, lista.getLastCodeUsedByColor(Colors.Verde) + 1))


# lista.inserirSemPrioridade(ListItem("A", 1))
# lista.inserirSemPrioridade(ListItem(Colors.Verde, 2))
# lista.inserirSemPrioridade(ListItem(Colors.Verde, 3))
# lista.inserirSemPrioridade(ListItem(Colors.Verde, 4))
# lista.inserirSemPrioridade(ListItem(Colors.Verde, 5))
# lista.inserirComPrioridade(ListItem(Colors.Verde, 201))

print(lista)
