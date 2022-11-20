from random import randint
from time import sleep
body_loto = []
regioes = ['Morro Rock', 'Rancho Coronado', 'Heywood', 'New Westbrook', 'Watson', 'Old Corp Center']

for c in regioes:
    d6 = randint(0,6)
    print(f'Em {c:.<20} {d6} mortes')
    body_loto.append(d6)

print(body_loto)
#print(sorted(body_loto))
soma = sum(body_loto)
print(soma)
