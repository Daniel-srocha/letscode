# Estruturas condicionais

idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.' )


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

media = (n1 + n2 + n3) / 3

if media >= 7:
    print('Você Passou!')
elif media < 5:
        print('Reprovado!')
else:
    print('Sua nota final foi', media, 'E você está de Recuperação!')
