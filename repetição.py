# Estrutura de repetição / Laço

n1 = int(input('Digite um número entre 1 e 10: '))
pc = 10
n2 = 0

while n1 != pc:
    print('errou!')
    n1 = int(input('Digite um número entre 1 e 10: '))
    n2 = n2 + 1
print('Parabéns! Você Acertou! com', n2 + 1, 'tentativas')

