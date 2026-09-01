from Ajudas import * 
clear()


class ListItem:
    def __init__(self, color, code):
       self.color = color
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
        nodo.color = "V"
              
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
        nodo.color = "A"
                
        if (self.head == None):
            self.head = nodo
            return
        
        current = self.head
        next = current.next
        
        # O primeiro já era verde, nesse caso, substituir o Head também
        if(current.color == "V"):
            nodo.next = current
            self.head = nodo
            return
        
        while True:
            # o próximo é verde. 
            # No atual (ainda A), referenciar o novo nodo.
            # No novo nodo, refereênciar o próximo, que é um V
            if (next.color == 'V'):
                nodo.next = next
                current.next = nodo
                return
            # Sem verdes, mas é o último. Adiciona no final simplesmente        
            elif (next == None):
                current.next = nodo
                return
          
            if(nodo.code == 201):
                print(next.color == 'V')
                print(next.color)
            current = next    
            next = current.next
        
    
    
    # SUPORTE (apenas facilitam)
    def getLastGreenCode():
        pass
    
    
    def __repr__(self):
        final_representation = ""
        
        if(self.head == None):
            return "None"
        
        current = self.head
        while current.next != None:
            final_representation += f"[{current.color}, {current.code}] "
            current = current.next
            
            
        
        return final_representation
    
        

lista = SimpleList()

lista.inserirSemPrioridade(ListItem("A", 1))
lista.inserirSemPrioridade(ListItem("V", 2))
lista.inserirSemPrioridade(ListItem("V", 3))
lista.inserirSemPrioridade(ListItem("V", 4))
lista.inserirSemPrioridade(ListItem("V", 5))
lista.inserirComPrioridade(ListItem("V", 201))


print(lista)
