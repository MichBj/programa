#Definimos la funcion de conversión
def conversor(grados):
    farenheit= (9/5)+(grados+32)#Formula Farenheit
    kelvin=273.15+grados #Formula Kelvin
    return farenheit, kelvin
grado_cen=int(input("Ingrese Grados: ")) #Definimos variable
RFare, Rkel=conversor(grado_cen)
#Imprimimos Resultado
print("Grados farenheit: ",RFare)
print("Grados kelvin: ",Rkel)
