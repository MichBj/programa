# Diccionario
informacion_personal = {
'Nombre':'Michael Bagui',
'Edad':27,
'Ciudad':'Quito',
'Provincia':'Pichincha',
}
print(informacion_personal)

# Modificar el valor
informacion_personal['Ciudad'] = input("Ingrese Ciudad:")
informacion_personal['Provincia'] = input("Ingrese Provincia:")
print(informacion_personal)

# Agregar nueva clave:valor
informacion_personal['Titulo'] = input("Ingrese Titulo: ")
print(informacion_personal)

# Verificar telefono y agregar
if 'Telefono' in informacion_personal:
 print(informacion_personal['Telefono'])
else:
 informacion_personal['Telefono'] = '0961518655'
print(informacion_personal)

# Eliminar edad
informacion_personal.pop('Edad')
print(informacion_personal)