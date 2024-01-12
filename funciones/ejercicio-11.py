# Escribir una función lógica vocal que determine si un carácter es una vocal.
    


def vocal(caracter):
    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
        print("el caracter es una vocal")
    else:
        print("no es vocal")

caracter = str(input("ingrese caracter: "))

vocal(caracter)