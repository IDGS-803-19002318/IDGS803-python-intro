num1 = int(input("Dame un numero: "))
num2 = int(input("Dame otro numero: "))

if(num1 > num2):
     print("{} es mayor que {}".format(num1,num2))
else:
     print("{1} es mayor que {0}".format(num1,num2))

print("-------------Dato Nuevo--------------------")

edad = int(input("Dame tu edad: "))

if edad > 18 :
     print("Eres mayor de edad")
elif edad == 18:
     print("Tienes 18")
else:
     print("Eres menor de edad")

