minha_lista1 = ["abacaxi", "melancia", "abacate"]
minha_lista2 = [1 ,2 ,3 ,4 , 5]
minha_lista3 = ["abacaxi", 2, 9.89, True]
minha_lista4 = []

print(minha_lista3)
print(minha_lista1[2])

for item in minha_lista1:
    print(item)

print(len(minha_lista1))

minha_lista1.append("limao")
print(minha_lista1)

if 3 in minha_lista2:
    print("3 esta na lista")

del minha_lista1[2:]
print(minha_lista1)

del minha_lista1[:]
print(minha_lista1)

minha_lista4.append(57)
print(minha_lista4)