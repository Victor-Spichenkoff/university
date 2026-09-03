from Ajudas import * 
clear()


class State:
    def __init__(self, sigla, full_name):
       self.sigla = sigla
       self.full_name = full_name
       self.next = None
       
    def __repr__(self):
        # Facilitar ver o meu estado
        if(self.sigla.upper() == "VS"):
            return f"\033[1;34;40m{self.sigla}\033[m"
        
        return f"{self.sigla.upper()}"
       
       
class SimpleList:
    head: State
    
    def __init__(self):
        self.head = None
        
    def inserirInicio(self, new_state: State):
        new_state.next = self.head
        self.head = new_state
        
    def __repr__(self):
        final_representation = ""
        
        current = self.head
        while current != None:
            final_representation += f"{current} -> "
            current = current.next
        
        return final_representation + "None"
    
    
class HashTable:
    list: list[SimpleList] = [ ]
    
    def __init__(self):
        for i in range(10):
            self.list.append(SimpleList())
        
    def funcaoHash(self, sigla):
        sigla = sigla.upper()# padronizado
        if sigla == "DF":
            return 7
        
        char1Ascii = ord(sigla[0])
        char2Ascii = ord(sigla[1])
        
        return (char1Ascii + char2Ascii) % 10

    def insertItem(self, sigla, full_name):
        state = State(sigla, full_name)
        hash = self.funcaoHash(sigla)
        
        self.list[hash].inserirInicio(state)

    def printList(self):
        count = 0
        for listItem in self.list:
            print(f"{count}: {listItem}")
            count+=1


hashList = HashTable()


# print vazio
hashList.printList()


# Esperar
input("\nAperte ENTER para seguir (adicionar estados)...")

# Inserindo todos os estados
hashList.insertItem("AC", "Acre")
hashList.insertItem("AL", "Alagoas")
hashList.insertItem("AP", "Amapá")
hashList.insertItem("AM", "Amazonas")
hashList.insertItem("BA", "Bahia")
hashList.insertItem("CE", "Ceará")
hashList.insertItem("DF", "Distrito Federal")
hashList.insertItem("ES", "Espírito Santo")
hashList.insertItem("GO", "Goiás")
hashList.insertItem("MA", "Maranhão")
hashList.insertItem("MT", "Mato Grosso")
hashList.insertItem("MS", "Mato Grosso do Sul")
hashList.insertItem("MG", "Minas Gerais")
hashList.insertItem("PA", "Pará")
hashList.insertItem("PB", "Paraíba")
hashList.insertItem("PR", "Paraná")
hashList.insertItem("PE", "Pernambuco")
hashList.insertItem("PI", "Piauí")
hashList.insertItem("RJ", "Rio de Janeiro")
hashList.insertItem("RN", "Rio Grande do Norte")
hashList.insertItem("RS", "Rio Grande do Sul")
hashList.insertItem("RO", "Rondônia")
hashList.insertItem("RR", "Roraima")
hashList.insertItem("SC", "Santa Catarina")
hashList.insertItem("SP", "São Paulo")
hashList.insertItem("SE", "Sergipe")
hashList.insertItem("TO", "Tocantins")


print("\nApós inserir tudo:")
hashList.printList()


# Esperar
input("\nAperte ENTER para seguir (inserir meu estado)...")



hashList.insertItem("VS", "Victor Spichenkoff Santana")

print("\nApós inserir meu estado:")
hashList.printList()