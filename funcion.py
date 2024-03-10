def calcut(ciudades, semanas, temperaturas):
    """
    Calcula la temperatura promedio de una ciudad durante un período de tiempo.
    Imprimir promedio de cada ciudad
    """
    promedios = {}
    for ciudad in ciudades:
        promedios[ciudad] = []
        for semana in semanas:
            # Obtener las temperaturas de la ciudad y semana actual
            temps = temperaturas[ciudad][semana]

            # Si no hay datos para la ciudad y semana actual, continuar
            if not temps:
                continue

            # Calcular el promedio de las temperaturas
            promedio = sum(temps) / len(temps)
            promedios[ciudad].append(promedio)
    return promedios


# Ejemplo de uso
ciudades = ["Loja", "Guayaquil", "Esmeraldas"]
semanas = [1, 2, 3, 4]
temperaturas = {
    "Loja": {
        1: [20, 5, 21, 1.9],
        2: [21, 23, 2.2, 20],
        3: [20, 12, 23, 21],
        4: [35, 25, 15, 19],
    },
    "Guayaquil": {
        1: [28, 29, 11, 26],
        2: [29, 30, 28, 27],
        3: [30, 18, 29, 0],
        4: [31, 32, 17, 29],
    },
    "Esmeraldas": {
        1: [18, 20, 19, 17],
        2: [19, 21, 20, 18],
        3: [20, 22, 21, 19],
        4: [21, 23, 22, 20],
    },
}

promedio = calcut(ciudades, semanas, temperaturas)

# Imprimir los promedios de cada ciudad
for city, promedia in promedio.items():
    print(f"Ciudad: {city}")
    for semana, promedios in enumerate(promedia):
        print(f"Semana {semana + 1}: {promedios:.2f}°C")
    print()