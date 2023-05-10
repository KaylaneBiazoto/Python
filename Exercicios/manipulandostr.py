str = 'Osmanthus wine tastes the same as I remember... But where are those who share the memory?'
print(str[3])
print(str[3:13])
print(str[:13])
print(str[13:])
print(str[1::2])
print(str.upper().count('O'))
print(str.replace('wine', 'beer')) # não muda a frase pq é imutável
str = str.replace('wine', 'beer') # agora mudou
print(str)
print('tastes' in str)
print(str.find('Osmanthus'))

print(str.split())
dividido = str.split() # Criou uma lista
print(dividido[0])
print(dividido[2][3])
