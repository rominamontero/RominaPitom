# print("13-04-2026")

# #Crenado variables

# titulo="Clima de hoy" #String
# diadelmes=13 #Int
# mes=4 #Int
# temperatura=22.3 #Float
# llueve=False #Boolean

# print(titulo)
# print("Temperatura actual: " ,temperatura, "grados")
# print(diadelmes, "-", mes)


# if llueve:
#     print("Tiene que llevar paraguas")
# else:
#     print("Puede llevar polera sin mangas")

# Pedir password y pin
# Pida al usuario password en palabra que debe ser "temu"
# ademas pida en pin que debe ser 3435
# los dos deben estar correctos para acceder al sistema



# pas=input("Ingrese su password: ")
# pin= int(input("Ingrese su pin: "))

# if pas == "temu" and pin == 3435:
#     print("Acceso concedido")
# else:
#     print("Algo salio mal")

ingreso=int(input("Ingrese su sueldo: "))

print("1.- Basico")
print("2.- Medio")
print("3.- Superior")
edu=int(input("Ingrese su nivel educacional: "))
nacionalidad= input("Ingrese nacionalidad (chilena/otra): ")

credito=0

if ingreso > 500000 and ingreso <=1000000:
    credito=credito+300000
elif ingreso > 1000001 and ingreso <1500000:
    credito=credito+650000
elif ingreso > 1500001:
    credito=credito+1000000
else:
    print("No tiene sueldo suficiente")

if edu ==1:
    print("No tiene beneficio por educacion")
elif edu==2:
    credito=credito*1,3
elif edu ==3:
    credito=credito*1.5

if nacionalidad =="chilena":
    credito=credito+300000
else:
    print("No tiene beneficio por nacionalidad")

print("Su puntaje de credito es: " ,credito)

    
