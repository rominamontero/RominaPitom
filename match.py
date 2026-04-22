#Ejemplo y explicacio  match




# total=0
# op=0

# while op != 4:
#     print("1.- Radio stereo sony $70.000")
#     print("2.- LGTV 55 pulgadas ultra gei $500.000")
#     print("3.- PS5 $580.000")
#     print("4.- Salir")
#     op=int(input())


#     match op:
#         case 1: 
#             print(" El precio a pagar es: ", 70000*1.19)
#             total+=70000+1.19
#         case 2: 
#             print("El precio a pagar es: ", 500000*1.19)
#             total+=500000*1.19
#         case 3:
#             print("El preio a pagar es: ", 580000*1.19)
#             total+=580000*1.19
#         case 4:
#             print("Saliendo") #Opcion con defecto
#         case _:
#             print("Op invalida")
#     print(f"Su total es: {total}")


# def suma():
#     num1= int(input("Ingrese el primer numero: "))
#     num2= int(input("Ingrese el segundo numero: "))            
#     print(f"La sume de sus numeros es: {num1+num2}")
# def resta():
#     num1= int(input("Ingrese el primer numero: "))
#     num2= int(input("Ingrese el segundo numero: "))
#     print(f"La resta de sus numeros es: {num1-num2}")
# def multi():
#     num1= int(input("Ingrese el primer numero: "))
#     num2= int(input("Ingrese el segundo numero: "))
#     print(f"La multiplicacion de sus numeros es: {num1*num2}")
# def division():
#     num1= int(input("Ingrese el primer numero: "))
#     num2= int(input("Ingrese el segundo numero: "))
#     print(f"La dividion de sus numeros es: {num1/num2}")




# op=0

# while op != 5:

#     op=int(input(''' Ingrese una operacion: 
#                 1.- Suma
#                 2.- Resta
#                 3.- Multiplicacion
#                 4.- Divivision
#                 5.- Salir
#                 '''))

#     match op != 5:
#         case 1: 
#             suma()
#         case 2: 
#             resta()
#         case 3:
#             multi()
#         case 4:
#             division() 
#         case 5:
#             print("Saliendo")
#         case _: 
#             print("Opcion invalida")



# name="romi"
# def saludo():
#     print("HolaAAAaaA, " ,name)

# def chao():
#     print("Ya nos vamos, " ,name)

# saludo()
# chao()

def promedio():
    nota=int(input("Ingrese la cantidad de notas"))
    suma=0

    for i in range(nota):
        n=float(input("Ingrese su nota:"))
        suma=n+suma
        prom= suma/nota
    print(f"Su promedio es {prom}")

def iva():
    n1=int(input("Ingrese el precio: "))
    print(f"El precio con iva es: {n1*1.19}")

def saludo():
    nombre=input("Ingrese su nombre:")
    print (f"Hola, {nombre}. Cmo le baila¿")


op=0

while op != 5:

    op=int(input(''' Ingrese una opcion: 
                1.- Sacar promedio
                2.- Calcular iva
                3.- Saludo
                4.- Salir
                '''))
    match op!= 4:
        case 1:
            promedio()
        case 2: 
            iva()
        case 3:
            saludo()
        case 4:
            print("Hasta la proximaa")
        case _:
            print("Opcion invalida")
