def calcular_puntaje(resp_alumno, resp_correcta):
    if resp_correcta == resp_alumno:
        return 4
    elif resp_alumno == "":
        return 0
    else:
        return -1

def calcular_nota(resp_correctas, resp_alumno):
    nota_final = 0
    for i in range(4):
        nota_final += calcular_puntaje(resp_alumno[i], resp_correctas[i])

    if nota_final < 0:
        nota_final = 0

    print(f'La nota final es: {nota_final}.')

calcular_nota(["a", "a", "b", "b"], ["a", "c", "b", "dq"])
calcular_nota(["a", "a", "c", "b"], ["a", "a", "b", ""])
calcular_nota(["a", "a", "b", "c"], ["a", "a", "b", "c"])
calcular_nota(["b", "c", "b", "a"], ["",  "a", "a", "c"])


    # nota_final += calcular_puntaje(resp_alumno[0], resp_correctas[0])
    # nota_final += calcular_puntaje(resp_alumno[1], resp_correctas[1])
    # nota_final += calcular_puntaje(resp_alumno[2], resp_correctas[2])
    # nota_final += calcular_puntaje(resp_alumno[3], resp_correctas[3])

    # if resp_correctas[0] == resp_alumno[0]:
    #     nota_final += 4
    # elif resp_alumno[0] == "":
    #     nota_final += 0
    # else:
    #     nota_final -= 1

    # if resp_correctas[1] == resp_alumno[1]:
    #     nota_final += 4
    # elif resp_alumno[1] == "":
    #     nota_final += 0
    # else:
    #     nota_final -= 1

    # if resp_correctas[2] == resp_alumno[2]:
    #     nota_final += 4
    # elif resp_alumno[2] == "":
    #     nota_final += 0
    # else:
    #     nota_final -= 1

    # if resp_correctas[3] == resp_alumno[3]:
    #     nota_final += 4
    # elif resp_alumno[3] == "":
    #     nota_final += 0
    # else:
    #     nota_final -= 1


