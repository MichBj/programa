# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)

#Empezamos definiendo las dimensiones
temperaturas = [
    [   # Ciudad 1 Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 21.5},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 26.5},
            {"day": "Domingo", "temp": 24}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 28.5},
            {"day": "Miércoles", "temp": 21.5},
            {"day": "Jueves", "temp": 20},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 18.9},
            {"day": "Domingo", "temp": 9.3}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 23.7},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 18.5},
            {"day": "Jueves", "temp": 28.2},
            {"day": "Viernes", "temp": 8.8},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 19}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 8.0},
            {"day": "Jueves", "temp": 7.9},
            {"day": "Viernes", "temp": 8.4},
            {"day": "Sábado", "temp": 8.7},
            {"day": "Domingo", "temp": 9.1}
        ]
    ],
    [   # Ciudad 2 Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 6.2},
            {"day": "Martes", "temp": 6.4},
            {"day": "Miércoles", "temp": 6.8},
            {"day": "Jueves", "temp": 7.0},
            {"day": "Viernes", "temp": 7.3},
            {"day": "Sábado", "temp": 7.5},
            {"day": "Domingo", "temp": 7.9}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 6.3},
            {"day": "Martes", "temp": 6.6},
            {"day": "Miércoles", "temp": 7.0},
            {"day": "Jueves", "temp": 7.2},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 6.1}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 6.1},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 38},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 10}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 39},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 4},
            {"day": "Sábado", "temp": 7.7},
            {"day": "Domingo", "temp": 8.0}
        ]
    ],
    [   # Ciudad 3 Loja
        [   # Semana 1
            {"day": "Lunes", "temp": 9.0},
            {"day": "Martes", "temp": 9.2},
            {"day": "Miércoles", "temp": 9.4},
            {"day": "Jueves", "temp": 9.1},
            {"day": "Viernes", "temp": 8.8},
            {"day": "Sábado", "temp": 8.5},
            {"day": "Domingo", "temp": 8.2}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 8.9},
            {"day": "Martes", "temp": 9.1},
            {"day": "Miércoles", "temp": 9.3},
            {"day": "Jueves", "temp": 9},
            {"day": "Viernes", "temp": 8.7},
            {"day": "Sábado", "temp": 8.4},
            {"day": "Domingo", "temp": 8.1}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 20.1},
            {"day": "Martes", "temp": 15},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 13}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 9},
            {"day": "Miércoles", "temp": 5.92},
            {"day": "Jueves", "temp": 19},
            {"day": "Viernes", "temp": 6},
            {"day": "Sábado", "temp": 8.3},
            {"day": "Domingo", "temp": 18.0}
        ]
    ]
]
# Calcular el promedio de temperaturas para cada ciudad y semana
# Realizamos un for aninado que nos dara el resultado
no_ciudad = 0
for ciudad in temperaturas:
    no_ciudad = no_ciudad + 1
    print(f'CIUDAD No. {no_ciudad}')
    no_semana = 0
    suma_promedio = 0
    for semana in ciudad:
        no_semana += 1
        suma = 0
        for dia in semana:
            suma = suma + dia['temp']
        promedio = round(suma / len(semana), 1)
        suma_promedio += promedio
        print(f'El promedio semana No. {no_semana} es: {promedio}')
    promedio_ciudad = round(suma_promedio / len(ciudad), 1)
    print(f'El promedio mensual es: {promedio_ciudad}')
