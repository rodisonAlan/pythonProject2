a = int(input('Primeiro bimenstre:'))
while a > 10:
   a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre:'))
while b > 10:
   b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre:'))
while c > 10:
   c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre:'))
while d > 10:
   d = int(input('Você digitou errado. Quarto bimestre: '))
media = (a + b + c + d)/4
print('media: {}'.format(media))




# nota = int(input('Entre com a nota: '))
# while nota > 10:                                               Usando while
#     nota = int(input("Nota inválida.Entre com a nota: "))
# a = 0
# while a < 10:
#     print(a)
#     a += 1




# a = int(input("Entre com um valor: "))
# for num in range(a+1):
#     div = 0
#     for x in range(1, num + 1):               Laco de repetição com for dentro do for
#         resto = num % x
#         # print(x, resto)
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)









# a = int(input('Entre com o número: '))
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x                       codigo com for in range numeros primos
#     print(x, resto)
#     if resto == 0:
#         div += 1
# if div == 2:
#     print('número {} é primo'.format(a))
# else:
#     print('número {} não é primo'.format(a))
