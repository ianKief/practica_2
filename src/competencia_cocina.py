def competencia():
    rounds = [
        {
    'theme': 'Entrada',
    'scores': {
    'Valentina': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},

    'Mateo': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},

    'Camila': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},

    'Santiago': {'judge_1': 6, 'judge_2': 7, 'judge_3': 6},

    'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 8},
            }
        },
        {
    'theme': 'Plato principal',
    'scores': {
    'Valentina': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},

    'Mateo': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},

    'Camila': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},

    'Santiago': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},

    'Lucía': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
            }
        },
        {
    'theme': 'Postre',

    'scores': {
    'Valentina': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},

    'Mateo': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},

    'Camila': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},

    'Santiago': {'judge_1': 7, 'judge_2': 7, 'judge_3': 6},

    'Lucía': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
            }
        },
        {
    'theme': 'Cocina internacional',
    'scores': {
    'Valentina': {'judge_1': 8, 'judge_2': 9, 'judge_3': 9},

    'Mateo': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},

    'Camila': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},

    'Santiago': {'judge_1': 8, 'judge_2': 9, 'judge_3': 7},

    'Lucía': {'judge_1': 7, 'judge_2': 7, 'judge_3': 8},
            }
        },
        {
    'theme': 'Final libre',
    'scores': {
    'Valentina': {'judge_1': 9, 'judge_2': 8, 'judge_3': 9},

    'Mateo': {'judge_1': 8, 'judge_2': 9, 'judge_3': 8},

    'Camila': {'judge_1': 7, 'judge_2': 7, 'judge_3': 7},

    'Santiago': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},

    'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 7},
            }
        }
    ]

    participantes = {}

    for i, ronda in enumerate(rounds):
        ganador_ronda = ""
        puntaje_max_ronda = -1
        print(f" Ronda {i + 1}: {ronda['theme']}")
        for participante, scores in ronda['scores'].items():
            # Para cada participante, me quedo con cada puntaje de cada juez y los sumo
            puntaje_ronda = sum(scores.values())
            print(f"  {participante}: {puntaje_ronda} puntos")
            if participante not in participantes:
                # Si el participante no esta en el diccionario, lo agrego con sus valores iniciales
                participantes[participante] = {'puntaje_total': 0, 'rondas_ganadas': 0, 'mejor_ronda': 0, 'promedio': 0}
            participantes[participante]['puntaje_total'] += puntaje_ronda
            if puntaje_ronda > puntaje_max_ronda:
                puntaje_max_ronda = puntaje_ronda
                ganador_ronda = participante
            if puntaje_ronda > participantes[participante]['mejor_ronda']:
                participantes[participante]['mejor_ronda'] = puntaje_ronda
        print()
        if ganador_ronda:
            print(f"  Ganador: {ganador_ronda} ({puntaje_max_ronda} pts)")
            participantes[ganador_ronda]['rondas_ganadas'] += 1
        print()
    # Ordeno la tabla de posiciones por puntaje total, de mayor a menor
    tabla_ordenada = sorted(participantes.items(), key=lambda x: (-x[1]['puntaje_total']))
    print("Tabla de posiciones final:")
    print(f"{'Participante':<15} {'Puntaje':<10} {'Rondas ganadas':<15} {'Mejor ronda':<15} {'Promedio':<10}")
    for participante, datos in tabla_ordenada:
        datos['promedio'] = datos['puntaje_total'] / len(rounds)
        print(f"{participante:<15} {datos['puntaje_total']:<10} {datos['rondas_ganadas']:<15} {datos['mejor_ronda']:<15} {datos['promedio']:<10.1f}")