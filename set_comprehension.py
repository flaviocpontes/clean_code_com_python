personagens = {'Aquaman': {'owner': 'DC'},
               'Superman': {'owner': 'DC'},
               'Wonder Woman': {'owner': 'DC'},
               'Iron Man': {'owner': 'Marvel'},
               'Spawn': {'owner': 'Image'},
               'Hulk': {'owner': 'Marvel'},
               'Witchblade': {'owner': 'Image'}}

personagens_dc = {personagem
                  for personagem in personagens
                  if personagens[personagem]['owner'] == 'DC'}

print(personagens_dc)
