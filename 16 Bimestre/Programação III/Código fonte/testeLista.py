from Ajudas import * 
clear()




class Item:
    def __init__(self, valor):
        self.dado = valor
        self.proximo = None
        
class ListaEncadeada:
    head: Item | None = None
    
    def __init__(self, *args, **kwds):
        self.head = None
        
    def AdicionarInicio(self, dado: Item):
        if(self.head == None):
            self.head = dado
            return
        
        dado.proximo = self.head
        self.head = dado
        
    def Show(self):
        dadoAtual = self.head
        while dadoAtual.proximo is not None:
            print(dadoAtual.dado)
            dadoAtual = dadoAtual.proximo
        print(dadoAtual.dado)
        
        
        
listaTeste = ListaEncadeada()
listaTeste.AdicionarInicio(Item(30))
listaTeste.AdicionarInicio(Item(21))
listaTeste.AdicionarInicio(Item(44))
listaTeste.AdicionarInicio(Item(33))


listaTeste.Show()        