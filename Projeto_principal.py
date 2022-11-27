import matplotlib.pyplot as plt # Biblioteca para gerar graficos.
from random import randrange, seed  # Podemos configurar o número inicial e sempre obter os mesmos valores na sequência. Teremos sempre o mesmo número aleatório gerado a partir deste valor inicial, que no caso será 9. Podemos utilizar o seed() para gerar valores diferentes pra nossa lista de notas, inclusive.

seed(11) 

randrange(0,11)

notas_matematica = []

for notas in range(8):
  notas_matematica.append(randrange(0,11))

x = list(range(1, 9)) # X do plano cartesiano.
y = notas_matematica # Y do plano cartesiano.
plt.plot(x, y, marker='o') # Gerador do grafico. este maker é a forma do indicador.
plt.title('Notas de matemática') # Titulo do grafico.
plt.xlabel('Provas') # Titulo do x
plt.ylabel('Notas') # Titulo do y
plt.show() # Tira todos os codigos da geração do grafico que é emitido.
