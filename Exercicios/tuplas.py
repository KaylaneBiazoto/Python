linha='='*50

episódios = ('Pilot', '0-8-4', 'The Asset', 'Eye Spy', 'Girl in the Flower Dress', 'FZZT', 'The Hub', 'The Well',

             'Repairs', 'The Bridge', 'The Magical Place', 'Seeds', 'Tracks', 'TAHITI', 'Yes Men', 'End of the Beginning',

             'Turn, Turn, Turn', 'Providence', 'The Only Light in the Darkness', 'Nothing Personal', 'Ragtag', 'Beginning of the End')

print(f'Episódios da primeira temporada Agents of S.H.I.E.L.D.: {episódios}')

print(linha)

print(f'Cinco primeiros episódios: {episódios[:5]}')

print(linha)

print(f'Os últimos 4 episódios: {episódios[-4:]}')

print(linha)

print(f'Episódios em ordem alfabética: {sorted(episódios)}')

print(linha)

print(f'O episódio Providence está na {episódios.index("Providence") + 1} posição')

print(linha)

ep = int(input('\n•Qual episódio [1 até 22] você deseja saber o nome?: '))

print(f'O episódio número \033[34m{ep}\033[m se chama \033[34m{episódios[ep-1]}')