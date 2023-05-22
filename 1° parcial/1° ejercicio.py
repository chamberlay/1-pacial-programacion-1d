#Crear una función llamada aplicarAumento que reciba como parámetro el precio de 
#un producto y devuelva el valor del producto con un aumento del 5%. Realizar la llamada desde el main.

def aumentar_precios(precio, porcentaje):
    precio_total = precio + precio * (porcentaje / 100)
    return precio_total

print(aumentar_precios(1000, 5))