from random import randint, choices
print(f'{" - BODY LOTTERY - ":$^32}')

body_loto = []
regioes = ['Morro Rock', 'Rancho Coronado', 'Heywood', 'New Westbrook', 'Watson', 'Old Corp Center']
for c in regioes:
    d6 = [0,1,2,3,4,5,6]
    final_d6 = choices(d6)
    if c == 'Morro Rock':
        final_d6 = choices(d6, weights = [10,35, 30, 10, 0.5, 0.5, 0.5])
        print(f'Em {c:.<20} {final_d6} mortes')
    elif c == 'Old Corp Center':
        final_d6 = choices(d6,weights = (0, 0.5, 0.5, 10, 10, 30, 40) )
        print(f'Em {c:.<20} {final_d6} mortes')
    else:
        final_d6 = choices(d6)
        print(f'Em {c:.<20} {final_d6} mortes')

    body_loto.append(final_d6)

print()
#soma = sum(body_loto)
#print(f'{soma} em 24 horas!')
print(f'Os números em ordem: {sorted(body_loto)}')
print("Lembrando que: caso voce seja um dos sortudes\na acertar os números e as regiões seu prêmio\né DOBRADO!")

#27.411.923 em NC, 24.670.721,7, 12.335.360,85(50), 6.167.680,425(25)
#22% abaixo de 18 anos
#15,4% acima de 65 anos