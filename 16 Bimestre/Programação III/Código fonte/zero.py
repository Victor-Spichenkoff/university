from Ajudas import * 
clear()

def fat(n):
    if(n <= 1):
        return 1
    
    return n * fat(n-1)

print(fat(5))

def fibo(pos):
    if(pos == 0):
        return 0
    
    if(pos == 1 or pos == 2):
        return 1
    
    return fibo(pos-1) + fibo(pos-2)



print(fibo(10))
inteiro = int(332)