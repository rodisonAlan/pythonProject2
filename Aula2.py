a = int(input('Primeiro bimenstre:'))
if a > 10:
   a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre:'))
if b > 10:
   b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre:'))
if c > 10:
   c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre:'))
if d > 10:
   d = int(input('Você digitou errado. Quarto bimestre: '))
media = (a + b + c + d)/4
print('media: {}'.format(media))
# if a <= 10 and b <= 10 and c <= 10 and d <=10:
#    print('media: {}'.format(media))
# else:
#    print('Foi informado alguma nota errada')
# a = int(input('Entre com um valor: '))
# b = int(input('Entre com um valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a  == 0 or resto_b == 0:                           Realizado uso do or
#     print('Foi digitado um número par')
# else:
#     print('Nenhum número par foi digitado')



# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor:'))
#
# if a > b and a > c:
#     print("O maior valor é {}" .format(a))
# elif b > a and b > c:
#     print("O maior valor é {}".format(b))
# else:
#     print("O maior valor é {}" .format(c))
#
# print('Final do programa')