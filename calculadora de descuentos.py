def calcular_descuento(monto_total, porcentaje_descuento=int(input("ingrese porcentaje de descuento: "))):
    """
    Calcula el descuento aplicado a un monto total de compra.

      monto_total: El monto total de la compra.
      porcentaje_descuento: El porcentaje de descuento a aplicar,
      En este caso se puede ingresar de manera manual el porcentaje a descontar
    Returns:
      El monto del descuento calculado.
    """

    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Llamadas a la función
# ingresamos de manera manual el monto de la compra
monto1 = int(input("ingrese valor de compra: "))
descuento_1 = calcular_descuento(monto1)
monto_final_1 = monto1 - descuento_1

monto2 = int(input("ingrese valor de segunda compra: "))
descuento_2 = calcular_descuento(monto2)
monto_final_2 = monto2 - descuento_2

# Salida de resultados
print(f"Compra 1: Monto total: ${monto1}")
print(f"Descuento aplicado: ${descuento_1}")
print(f"Monto final a pagar: ${monto_final_1}")

print(f"Compra 2: Monto total: ${monto2}")
print(f"Descuento aplicado: ${descuento_2}")
print(f"Monto final a pagar: ${monto_final_2}")
