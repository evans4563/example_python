#ejercicio targeta de crédito

precio_papas = float (10000)
precio_zanahoria = float (2000)
precio_carne = float (50000)
id_targeta = float (544356123010621)
saldo_targeta = float (7254000)
total_a_pagar = (precio_carne + precio_papas + precio_zanahoria)
saldo_restante = (saldo_targeta - total_a_pagar)

print ("factura:")
print ("La targeta", id_targeta, "con el saldo $", saldo_targeta, "realizó el siguiente movimiento:")
print ("papas= $", precio_papas)
print ("papas= $", precio_zanahoria)
print ("papas= $", precio_carne)
print ("total a pagar= $", total_a_pagar)
print ("el saldo restante de su targeta es: $", saldo_restante) 
print ("que disfrute sus productos, att tiendas DollarOlimpica")