def sumar(x, y):
    return x+y

print(sumar(5,5))

def restar(x, y):
    return x-y

print(restar(9,3))

def multiplicar(x, y):
    return x*y

print(multiplicar(5,5))

def dividir(x, y):
    return x/y

print(dividir(20,5))
  
menu = int(input("Menu:\n 1.-Sumar\n2.-Restar\n3.-Multiplicar\n4.-Dividir\nIngresa la opción deseada"))

if menu == 1:
    x = int(input("Ingresa el primer valor: "))
    y = int(input("Ingresa el segundo valor: "))
    print(sumar(x,y))
elif menu == 2:
    x = int(input("Ingresa el primer valor: "))
    y = int(input("Ingresa el segundo valor: "))
    print(restar(x,y))
elif menu == 3:
    x = int(input("Ingresa el primer valor: "))
    y = int(input("Ingresa el segundo valor: "))
    print(multiplicar(x,y))
elif menu == 4:
    x = int(input("Ingresa el primer valor: "))
    y = int(input("Ingresa el segundo valor: "))
    print(dividir(x,y))
else:
    print("Opcion no valida, intente de nuevo.")