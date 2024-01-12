import random

def Nivel(N):
    Mi_numero = 0
    Num1 = 0
    Limite = 0
    Chances = 0
    N_conv = int(N)
    
    Limite = 10 ** N_conv
    Chances = 5 * N_conv
    Mi_numero = random.randint(1, Limite)
    
    print("Elegiste el Nivel:", N, ", tienes que adivinar un número del 1 hasta el", Limite, ". Chances que tienes:", Chances)
    # print(Mi_numero)
    print("Ingresa un número")
    Num1 = int(input())
    
    while Mi_numero != Num1 and Chances > 1:
        if Mi_numero > Num1:
            print("Tu número es más bajo")
        else:
            print("Tu número es más alto")
        
        Chances -= 1
        print("Te quedan", Chances, "chances")
        Num1 = int(input())
    
    if Mi_numero == Num1:
        print("Adivinaste con", Chances-1, "chances a favor")
    else:
        print("Lo lamento, Alpiste... perdiste")

def Menu():
    print("Elige un nivel")
    print("1 - Fácil (1 - 10)")
    print("2 - Medio (1 - 100)")
    print("3 - Difícil (1 - 1000)")

def Opcion_nivel():
    N = ""
    
    while N != "1" and N != "2" and N != "3":
        N = input()
        
        if N == "1":
            Nivel(N)
        elif N == "2":
            Nivel(N)
        elif N == "3":
            Nivel(N)
        else:
            print("Opción incorrecta")
            input("Presione una tecla para continuar")

def Jugar(opc_bo):
    Opc = ""
    
    print("¿Podrás adivinar mi número? (S/N)")
    Opc = input()
    
    while Opc == "S" or Opc == "s":
        opc_bo = True
        Menu()
        Opcion_nivel()
        print("¿Quieres seguir jugando? (S/N)")
        Opc = input()

def Final(Opc_bo):
    if Opc_bo:
        print("Me tienes miedo...")
    else:
        print("Gracias por jugar")
        
def Adivinar_numero():
    Opc_bo = False
    Jugar(Opc_bo)
    Final(Opc_bo)

Adivinar_numero()