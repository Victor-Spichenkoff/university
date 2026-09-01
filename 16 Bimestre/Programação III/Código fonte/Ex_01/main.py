from Ajudas import * 
clear()
# TODO:
# - getLastGreen position não está funcionando. arrumar e tornar apra o yellow também 



from enum import Enum, auto


##############################################
# AJUDAS
##############################################
class Color(Enum):
    A = auto()
    V = auto()
    

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
    def __init__(self, color: Color, code):
       self.color: Color = color
       self.code = code
       self.next = None
       
       
    def __repr__(self):
        return f"[{self.color}, {self.code}]"
       
       
class SimpleList:
    head: ListItem
    
    def __init__(self):
        self.head = None
        
    
    # Sempre no final (V)
    def inserirSemPrioridade(self, nodo: ListItem):
        if(nodo.code > 200):
            return print("Itens sem prioridade não podem ter código maior que 200.")
        nodo.color = Color.V
              
        if (self.head == None):
            self.head = nodo
            return
        
        current = self.head
        next = current.next
        while True:
            # Sem validação especial, sempre vai ser o último
            if (next == None):
                current.next = nodo
                return
            current = next    
            next = current.next
        
    
    def inserirComPrioridade(self, nodo: ListItem):
        if(nodo.code < 201):
            return print("Itens COM prioridade não podem ter código menor que 201.")
        nodo.color = Color.A
                
        if (self.head == None):
            self.head = nodo
            return
        
        current = self.head
        next = current.next
        
        # O primeiro já era verde, nesse caso, substituir o Head também
        if(current.color is Color.V):
            nodo.next = current
            self.head = nodo
            return
        
        while True:
            # o próximo é verde. 
            # No atual (ainda A), referenciar o novo nodo.
            # No novo nodo, refereênciar o próximo, que é um V
            if (next.color is Color.V):
                nodo.next = next
                current.next = nodo
                return
            # Sem verdes, mas é o último. Adiciona no final simplesmente        
            elif (next == None):
                current.next = nodo
                return
          
            if(nodo.code == 201):
                print(next.color is Color.V)
                print(next.color)
            current = next    
            next = current.next
        
    
    
    # SUPORTE (apenas facilitam)
    def getLastGreenCodeUsed(self):
        if(self.head == None):
            return 0
        elif(self.head.next == None and self.head.color is Color.V):
            return 1
        elif(self.head.next == None):
            return 0
        
        current = self.head.next
        while True:
            if(current.next == None and current.color is Color.V):
                return current.code
            elif(current.next == None):
                return 0
        
    
    
    def __repr__(self):
        final_representation = ""
        
        if(self.head == None):
            return "None"
        
        current = self.head
        while current.next != None:
            final_representation += f"[{current.color.name}, {current.code}] "
            current = current.next
            
            
        
        return final_representation
    
        

lista = SimpleList()

lista.inserirSemPrioridade(ListItem("A", lista.getLastGreenCodeUsed() + 1))
lista.inserirSemPrioridade(ListItem(Color.V, lista.getLastGreenCodeUsed() + 1))
lista.inserirSemPrioridade(ListItem(Color.V, lista.getLastGreenCodeUsed() + 1))
lista.inserirSemPrioridade(ListItem(Color.V, lista.getLastGreenCodeUsed() + 1))
lista.inserirSemPrioridade(ListItem(Color.V, lista.getLastGreenCodeUsed() + 1))
lista.inserirComPrioridade(ListItem(Color.V, 201))


# lista.inserirSemPrioridade(ListItem("A", 1))
# lista.inserirSemPrioridade(ListItem(Color.V, 2))
# lista.inserirSemPrioridade(ListItem(Color.V, 3))
# lista.inserirSemPrioridade(ListItem(Color.V, 4))
# lista.inserirSemPrioridade(ListItem(Color.V, 5))
# lista.inserirComPrioridade(ListItem(Color.V, 201))

print(lista)
