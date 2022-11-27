permissoes = []
idades = [20, 14, 40]  

'''def verifica_se_pode_dirigir(idades, permissoes):
    for idade in idades:
        if idade >= 18:
            permissoes.append(True)
        else:
            permissoes.append(False)

for permissao in permissoes:
    if permissao == True:
        print('Tem permissão para dirigir')
    else:
        print('Não tem permissão para dirigir')

verifica_se_pode_dirigir(idades, permissoes)'''

def verifica_se_pode_dirigir(idades):
  
  for idade in idades:
    
    if idade >= 18:
      print(f'{idade} anos, Tem permissão')
    
    else:
      print(f'{idade} anos, Não tem permissão')

verifica_se_pode_dirigir(idades)
