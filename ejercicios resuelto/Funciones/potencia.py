def potencia(base,exp):
    pot=1
    for i in range (1,exp+1):
        pot=base*pot
    return pot

base=int(input ("ingrese base: "))
exp=int(input ("ingrese exponente: "))
res=potencia(base,exp)
print(res)