# DISSECANDO UMA VARIÁVEL

a = input('Digite algo: ')

print('O tipo primitivo desse valor é:', type(a))

print('Só tem espaços?:', 'Sim.' if a.isspace() else 'Não.')

print('É um numero?:', 'Sim.' if a.isnumeric() else 'Não.')

print('É um alfabético?:', 'Sim.' if a.isalpha() else 'Não.')

print('É um alfanumérico?:', 'Sim.' if a.isalnum() else 'Não.')

print('Está em maiúsculo?:', 'Sim.' if a.isupper() else 'Não.')

print('Está em minúsculo?: ', 'Sim.' if a.islower() else 'Não.')

print('Está capitalizada?:', 'Sim.' if a.istitle() else 'Não.')
