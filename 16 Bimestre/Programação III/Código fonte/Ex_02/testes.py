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
            return f"\033[1;31;40m{self.sigla}\033[m"
        
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
    
        

def funcaoHash(sigla):
    sigla = sigla.upper()# padronizado
    if sigla == "DF":
        return 7
    
    char1Ascii = ord(sigla[0])
    char2Ascii = ord(sigla[1])
    
    return (char1Ascii + char2Ascii) % 10


full_list: list[SimpleList] = []
for i in range(10):
    full_list.append(SimpleList())


def insertOnList(sigla, full_name):
    state = State(sigla, full_name)
    hash = funcaoHash(sigla)
    
    full_list[hash].inserirInicio(state)


def printList(lista: list[SimpleList]):
    count = 0
    for listItem in lista:
        print(f"{count}: {listItem}")
        count+=1


# print vazio
printList(full_list)


# Esperar
input("\nAperte ENTER para seguir (adicionar estados)...")

# Inserindo todos os estados
insertOnList("AC", "Acre")
insertOnList("AL", "Alagoas")
insertOnList("AP", "Amapá")
insertOnList("AM", "Amazonas")
insertOnList("BA", "Bahia")
insertOnList("CE", "Ceará")
insertOnList("DF", "Distrito Federal")
insertOnList("ES", "Espírito Santo")
insertOnList("GO", "Goiás")
insertOnList("MA", "Maranhão")
insertOnList("MT", "Mato Grosso")
insertOnList("MS", "Mato Grosso do Sul")
insertOnList("MG", "Minas Gerais")
insertOnList("PA", "Pará")
insertOnList("PB", "Paraíba")
insertOnList("PR", "Paraná")
insertOnList("PE", "Pernambuco")
insertOnList("PI", "Piauí")
insertOnList("RJ", "Rio de Janeiro")
insertOnList("RN", "Rio Grande do Norte")
insertOnList("RS", "Rio Grande do Sul")
insertOnList("RO", "Rondônia")
insertOnList("RR", "Roraima")
insertOnList("SC", "Santa Catarina")
insertOnList("SP", "São Paulo")
insertOnList("SE", "Sergipe")
insertOnList("TO", "Tocantins")


print("\nApós inserir tudo:")
printList(full_list)


# Esperar
input("\nAperte ENTER para seguir (inserir meu estado)...")



insertOnList("VS", "Victor Spichenkoff Santana")

print("\nApós inserir meu estado:")
printList(full_list)