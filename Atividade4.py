v1 = 0
v2 = 0
v3 = 0
v4 = 0

for i in range(4):
    candidato = input("1-Joaquin  2-Luul  3-Bonoro 4-Padre Kelvin\n")
    
    match candidato:
        case "1":
            print("Você escolheu o joaquin, Parabens!")
            v1+=1
        case "2":
            print("Você escolheu o luul, seu fudido, sem pai, sem mãe")
            v2+=1
        case "3":
            print("Você escolheu o bonoro, quer atirar nas pessoas?")
            v3+=1
        case "4":
            print("Você escolheu o Padre Kelvin, Amem")    
            v4+=1
        case _:
            print("Voto invalido")

        
print(f"O candidato Joaquin teve {v1} votos")
print(f"O candidato Luul teve {v2} votos")
print(f"O candidato Bonoro teve {v3} votos")
print(f"O candidato Padre Kelvin teve {v4} votos")
