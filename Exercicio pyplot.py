import matplotlib.pyplot as plt

notas_matematica = ['Matemática',8,7,6,6,7,7,8,10]
notas_portugues = ['Português',9,9,9,8,5,6,8,5]
notas_geografia = ['Geografia',10,10,6,7,7,7,8,7]

notas = [notas_matematica, notas_portugues, notas_geografia]

for nota in notas:
 x = list(range(1, 9)) # Cria uma lista com 9 números.
 y = nota[1:] # A partir do indice 1, é amarzenado as notas de cada materia.
 plt.plot(x, y, marker='o') # Gerador de lista.
 plt.xlabel('Provas') # Titulo de x
 plt.ylabel('Notas') # Titulo de y
 plt.title(nota[0]) # O titulo é gerado, pelo numero de graficos armazenados.
 plt.show() # Todos os codigos da geração do grafico, são excluidos.