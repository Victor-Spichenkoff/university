from Ajudas import * 
clear()
# TODO:
# - Não está salvando o último elemento, seja com ou sem prioridade



from enum import Enum, auto


##############################################
# AJUDAS
##############################################
class Colors(Enum):
    Amarelo = auto()
    Verde = auto()
    

##############################################
# MENUS
##############################################
def showMainMenuAndGetOption():
    print("=========================")
    print("[ 1 ] Adicionar paciente a fila")
    print("[ 2 ] Mostrar TODOS pacientes na fila")
    print("[ 3 ] Chamar próximo paciente")
    print("[ 4 ] Sair")
    result = int(input("Escolha uma opção: "))
    if(result > 4 or result <= 0):
        print("\nTENTE NOVAMENTE")
        return showMainMenuAndGetOption()
    if(result == 4):
        print("\n\nAdeus!")
        exit
    
    return result
    

# showMainMenuAndGetOption()




##############################################
# LISTAS    
##############################################

class ListItem:
    def __init__(self, color: Colors, code):
       self.color: Colors = color
       self.code = code
       self.next = None
       
       
    def __repr__(self):
        return f"[{self.color}, {self.code}]"
       
       
class SimpleList:

    def __init__(self):
        self.head = None
        
    
    # Sempre no final (V)
    def inserirSemPrioridade(self, nodo: ListItem):
        if(nodo.code > 200):
            return print("Itens sem prioridade não podem ter código menor que 200.")
        nodo.color = Colors.Verde
              
        if (self.head is None):
            self.head = nodo
            return
        
        current = self.head

        while current.next is not None:
            # Sem validação especial, sempre vai ser o último
            current =  current.next
            
        current.next = nodo
        
    
    def inserirComPrioridade(self, nodo: ListItem):
        if(nodo.code < 201):
            return print("Itens COM prioridade não podem ter código maior que 201.")
        nodo.color = Colors.Amarelo
                
        if (self.head is None):
            self.head = nodo
            return
        
        current = self.head
        next = current.next
        
        # O primeiro já era verde, nesse caso, substituir o Head também
        if(current.color is Colors.Verde):
            nodo.next = current
            self.head = nodo
            return
        
        while True:
            # Sem verdes, mas é o último. Adiciona no final simplesmente        
            if (next is None):
                current.next = nodo
                return
            # o próximo é verde. 
            # No atual (ainda A), referenciar o novo nodo.
            # No novo nodo, refereênciar o próximo, que é um V
            elif (next.color is Colors.Verde):
                current.next = nodo
                nodo.next = next
                return

            current = next    
            next = current.next
        
    
    
    # SUPORTE (apenas facilitam)
    def getLastCodeUsedByColor(self, targetColor: Colors):
        base = 0 if targetColor is Colors.Verde else 200

        if self.head is None:
            return base

        if targetColor is Colors.Verde: # Verde é sempre o final, so ir até o último
            current = self.head
            while current.next is not None:
                current = current.next
            return current.code if current.color is targetColor else base
        else: # Amarelo é sempre o início, parar no primeiro que não é amarelo
            if self.head.color is not targetColor:
                return base
            current = self.head
            while current.next is not None and current.next.color is targetColor:
                current = current.next
            return current.code
    
    
    def __repr__(self):
        final_representation = ""
        
        if(self.head == None):
            return "None"
        
        current = self.head
        while current != None:
            final_representation += f"[{current.color.name[0]}, {current.code}] "
            current = current.next
        
        return final_representation
    
        

lista = SimpleList()




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
