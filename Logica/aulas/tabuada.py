final = int(input("Até qual: ")) + 1

for i in range(1, final):
    print("-" * 15)
    print(f'Tabuada do {i}')
    for n in range(1, 11):
        print(f"{i} X {n} = {i * n}")
