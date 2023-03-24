from time import sleep
from random import randint

print('Vou pensar em um número entre 1 e 10, tente adivinhar!')
num = randint(1, 10) # Gera de 0 a 10

chute = int(input('Que número eu pensei? '))

print('Processando......')
sleep(0.5)

print(f'Ganhei! O número era {num}, não {chute}' if num != chute else 'Perdi! O número que você adivinhou está correto.')

