#Las tuplas no se pueden modificar, son como una constante

tupla = (1,2,3,4)

print(type(tupla))
print(tupla)

tupla2 = (7,"Roberto",True,23.9,12+3j)
print(tupla2)

tupla3 = tupla + tupla2
print(tupla3)

print(tupla2[1])
print(tupla[:])
print(tupla2[:4])
print(tupla2[0:])
print(tupla2[-1]) #trae el ultimo

a,b,c = tupla #Destructuracion de los datos