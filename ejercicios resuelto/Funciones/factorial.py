def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

num=int(input ("ingrese numero: "))
x=factorial(num)
print(x)
