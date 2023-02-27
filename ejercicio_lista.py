#examples of list
"""nombres = ["jesus", "Maria", "jose"] forma de lista
print (nombres[1])
"""


#datos_personas = {"jesus", 33, 1.75, True}
#print (datos_personas) 
#en forma de tupla



"""datos_personas = {
    "nombre" : "jesus", 
    "edad" : 33,
    "estatura" : 1.75,
    "¿soltero?" : True
}
print (datos_personas)
En forma de diccionario
"""

#en forma de tupla
#nombres = ["jesus", "Maria", "jose"]
#print (nombres[2])

#price = [100, 250, 300]
#resultado = price [0] + price [2]
#print ("el cliente", nombres[0], "pagó $", resultado)
#print (price[0], price [2])
















articulo = ["Zapatos", "Tenis", "Camisetas", "Jeans"]
Precio_de_venta = [350000, 280000, 175000, 200000]
costo_total = Precio_de_venta[0]+ Precio_de_venta[1]+ Precio_de_venta[2]+ Precio_de_venta[3]
aumento_jeans = float (0.062 * Precio_de_venta[3] + Precio_de_venta[3])
precio_zapatos = float (Precio_de_venta[0]- 0.008 * Precio_de_venta[0])
print (articulo[0],"cuestan: $", Precio_de_venta[0])
print (articulo[1], "cuestan: $", Precio_de_venta[1])
print (articulo[2], "cuestan: $", Precio_de_venta[2])
print (articulo[3], "cuestan: $", Precio_de_venta[3])


print ("costo total de todos los productos = $", costo_total)

print ("nuevo costo de jeans:")
print ("antes: $", Precio_de_venta[3])
print ("ahora: $", aumento_jeans)

print ("nuevo costo de Zapatos:")
print ("antes: $", Precio_de_venta[0])
print ("ahora: $", precio_zapatos)

