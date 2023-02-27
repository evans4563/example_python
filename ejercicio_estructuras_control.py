accion_uno = "Ya estoy en la entrada del evento"
accion_dos = "Me estoy registrando"

#estructura de control (condicional if o si)
#Permite continuar un flujo (realizar algo) si se cumple una condicion
# y en caso de no cumplirse, se puede o no continuar con otro flujo (realizar otra acción)
"""
estructura_datos_uno =  
estructura_datos_dos=
if estructura_datos_uno < estructura_datos_dos
if estructura_datos_uno > estructura_datos_dos
if estructura_datos_uno <= estructura_datos_dos
if estructura_datos_uno >= estructura_datos_dos
if estructura_datos_uno == estructura_datos_dos
if estructura_datos_uno != estructura_datos_dos
"""


#dato_comparacion = 18
#edad = 12
#if simple
"""
if edad >= dato_comparacion:
    print ("ingresar, good luck")
    """

#if compuesto   
"""
if edad >= dato_comparacion:
    print ("ingresar, good luck")
else: 
    print ("pa casa puñetas")
    """
#if anidado 

#boleta = False 
#if edad >= dato_comparacion and boleta:
 #   print ("ingresar, good luck")
#else: 

#    print ("pa casa puñetas")

localidades = """
opciones
1- VIP
2- Preferencial
3- General
4- Baja
"""
print (localidades)

op = int (input("que voleta deseas"))
if op is 1:
    print ("precio: $", 500)
elif op is 2:
    print ("precio: $", 400)
elif op is 3: 
    print ("precio: $", 300)
elif op is 4:
    print ("precio: $", 100)