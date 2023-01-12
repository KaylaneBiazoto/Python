from math import sin, cos, tan, radians

ang = float(input('Angulo: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tang = tan(radians(ang))
print(f'O ângulo de {ang} tem o seno {seno:.2f} cossenho {cosseno:.2f} e tangente {tang:.2f}')
