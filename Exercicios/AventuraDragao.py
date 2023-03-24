import time

print('Vamos cavaleiro, Venha lutar ao meu lado contra o dragão!')

nome = input('Me diga qual seu nome primeiro:  ')
print(f'Certo, {nome}, vamos lutar contra o dragão agora!')

time.sleep(2)

# Vida do Dragão
vd = int(2000)

# Ataque do Dragão
atkd = int(100)

# Vida do Player
vp = int(100)

# Ataque do Player
atkp = int(500)

# Defesa do Player
dfp = int(60)

print(f'~ {nome} ataca ~')
time.sleep(1.3)
vd = (vd - atkp)
print(f'A vida dele é {vd}')

time.sleep(1.3)
print('~ Dragão ataca ~')
pd = (atkd - dfp)
vp = (vp - pd)
time.sleep(1.3)
print(f'Sua vida cai para: {vp}')


time.sleep(1.3)
print(f'~ {nome} Tenta acertar um golpe duplo! ~')
time.sleep(1.3)
vd = (vd - atkp)
vd = (vd - atkp)
print(f'Você conseguiu acertas o golpe duplo! Agora a vida dele é {vd}!')

time.sleep(1.3)
print('~ Dragão ataca ~')
time.sleep(1.3)
vp = (vp - pd)
print(f'Você está à beira da morte, com {vp} de vida, você terá que dar o golpe final')

time.sleep(1.3)
print(f'~ {nome} Corta a cabeça do dragão com um golpe final ~')
vd = (vd - atkp)
time.sleep(1.3)

print(f'Você venceu! Agora o reino está a salvo graças a você!')
