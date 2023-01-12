num = int(input('Digite um número: '))

print('''Escolha uma das bases para a conversão:
[0] BINÁRIO
[1] OCTAL
[2] HEXADECIMAL ''')

opcao = int(input('Sua opção: '))

if opcao == 0:
    bin = bin(num)[2:]
    print(f'O número {num} convertido para binário é {bin}')
elif opcao == 1:
    octal = oct(num)[2:]
    print(f'O número {num} convertido para octal é {oct}')
elif opcao == 2:
    hexadecimal = hex(num)[2:]
    print(f'O número {num} convertido para hexadecimal é {hexadecimal}')
else:
    print('O número digitado não é válido.')