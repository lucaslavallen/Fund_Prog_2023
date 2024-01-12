#define un diccionario=registro con cuatro campos
persona={'nombreyap':'', 'dni':'', 'domicilio':'','edad':''}

#muestra el registro completo
print(persona)

#carga un diccionario=registro con cuatro campos
persona['nombreyap']=input('ingrese nombre y apellido: ')
persona['edad']=input('ingrese edad: ')
persona['domicilio']='henry 633'
persona['edad']=60

#agrega un campo
persona['profesión']='médica'
print(persona)

#elimina el campo domicilio del diccionario
del persona['domicilio'] 
print(persona)

#muestra campos del registro
print('La cantidad de campos del registro es : ',len(persona))

#muestra en pantalla cada uno de los campos
for campo in persona:
    print ('el campo', campo, 'es', persona[campo])
