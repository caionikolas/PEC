valor01 = input("Digite o valor 1: ")
valor02 = input("Digite o valor 2: ")
soma = float(valor01) + float(valor02)
concatenacao = str(float(valor01)) + valor02
multiNumber = float(valor01) * float(valor02)
multiString = str(float(valor01)) * int(valor02)
divisao = float(valor01) / float(valor02)
divisaoInteira = float(valor01) // float(valor02)
Expor = float(valor01) ** float(valor02)
resto = float(valor01) % float(valor02)
print('A some dos valores é {}!\n Sua concatenação {}!\n A multiplicação entre os dois valores é {}! \nA multiplicação dos valores como strings é {}!\nA divisão entre os valores é {}!\nA divisão inteira entre os valores é {}!\nA exponeciação do primeiro valor elevado ao segundo é {}!\nO resto da divisão entre os valores é {}!'.format(soma, concatenacao, multiNumber, multiString, divisao, divisaoInteira, Expor, resto))