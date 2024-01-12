vector=[4,7,1,2]

def ord (vector):
    for i in range (vector -1):
        for j in range (vector -1-i):
            if vector[j] < vector[j+1]:
                aux = vector[j]
                vector[j]=vector[j+1]
                print(vector)


ord(vector)
