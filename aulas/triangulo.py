
def is_valid(l1, l2, l3):   
    is_sizes_valid =  l3 + l2 > l1 and l1 + l3 > l2 and l1 + l2 > l3
    is_not_zero = l1 != 0 and l2 != 0 and l3 != 0
    
    return is_sizes_valid and is_not_zero  



def give_Triangle_type(l1, l2, l3):
   if(not is_valid(l1, l2, l3)):
       return "Inválido!"
   
   if l1 == l2 and l2 == l3:
      return "Equilátero"
   elif l1 == l2 or l2 == l3 or l1 == l3:
      return "Isósceles"
   
   return "Escaleno"

print(give_Triangle_type(0, 12, 12))

