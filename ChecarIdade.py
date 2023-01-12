from datetime import date

ano = int(input('Ano de nascimento: '))

idade = date.today().year - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {date.today().year}.')

if idade < 19:
    falta = 19 - idade
    print(f'Ainda falta {falta} anos para o alistamento.')
    print(f'O seu alistamento será em {date.today().year + falta}')
else:
    print(f'Você já pode se alistar!')
