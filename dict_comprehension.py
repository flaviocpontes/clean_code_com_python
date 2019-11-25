pessoas = ['Clark Kent', 'Bruce Wayne', 'Bruce Banner',
           'Steve Rogers', 'Barry Allen', 'Tony Stark']
herois = ['Superman', 'Batman', 'Hulk', 'Captain America',
          'Flash', 'Iron Man']

herois_dc = {'Superman', 'Batman', 'Wonder Woman', 'Flash',
             'Green Lantern', 'Nightwing'}

identidades_secretas = {}
for (pessoa, heroi) in zip(pessoas, herois):
    if heroi in herois_dc:
        identidades_secretas[heroi] = pessoa

print(identidades_secretas)

print({hero: person for person, hero in zip(pessoas, herois) if hero in herois_dc})












herois_marvel = {'Black Widow', 'Ant-Man', 'Hulk', 'Captain Marvel', 'Captain America', 'Iron Man', 'Vision'}
