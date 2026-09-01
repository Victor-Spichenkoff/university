def showMainMenu():
    print("=========================")
    print("[ 1 ] Adicionar paciente a fila")
    print("[ 2 ] Mostrar TODOS pacientes na fila")
    print("[ 3 ] Chamar próximo paciente")
    print("[ 4 ] Sair")
    result = int(input("Escolha uma opção: "))
    if(result > 4 or result <= 0):
        print("\nTENTE NOVAMENTE")
        return showMainMenu()
    if(result == 4):
        print("\n\nAdeus!")
        exit
    
    return result
    

showMainMenu()