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



pas=input("Ingrese su password: ")
pin= int(input("Ingrese su pin: "))

if pas == "temu" and pin == 3435:
    print("correcto")
else:
    print("incorrecto")