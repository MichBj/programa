# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1
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
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 78},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 84},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 91}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 62},
            {"day": "Martes", "temp": 64},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 75},
            {"day": "Domingo", "temp": 79}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 63},
            {"day": "Martes", "temp": 66},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 61},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 72},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 80}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 64},
            {"day": "Martes", "temp": 67},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 80}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 92},
            {"day": "Miércoles", "temp": 94},
            {"day": "Jueves", "temp": 91},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 82}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 89},
            {"day": "Martes", "temp": 91},
            {"day": "Miércoles", "temp": 93},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 84},
            {"day": "Domingo", "temp": 81}
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
