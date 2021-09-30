lista = [12, 10, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante','lobo',  'arara']

lista_animal  [0] = 'macaco'
print(lista_animal)

tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica [0] = 100
print(lista_numerica)


# print(lista [1])
# nova_lista = lista_animal * 3              CONSIGO USANDO O IF MULTIPLICAR ESSA LISTA
# print(nova_lista)


# lista.sort()
# lista_animal.sort()        usando o .sort ele ordena a lista
# print(lista)
# print(lista_animal)
# lista_animal.reverse()     usando o .reverse ele ordena de tras para frente
# print(lista_animal)





# if 'ovelha' in lista_animal:
#     print('Existe um ovelha na lista')
# else:
#     print('Não existe um ovelha na lista. Será incluido')
#     lista_animal.append('ovelha')           usando o . append inclui um item novo na lista
#     print(lista_animal)




    # lista_animal. pop(0)
    # print(lista_animal)      usando o pop para remover , e se colocar o valor ele tirá o que está na posiçao

    # lista_animal. remove('elefante')
    # print(lista_animal)               usando o . remove ele retira o próprio item da lista


# lista = [1, 3, 5, 7]
# lista_animal = ['cachorro', 'gato', 'elefante']
# # print(lista [1])
#                                            fazer a verificação do maior ou menor usando Max ou Min
# print(max(lista_animal))


# lista = [1, 3, 5, 7]
# lista_animal = ['Leao', 'elefante', 'gato']
# print(lista_animal [1])                           Vai apenas passar pela lista
#
# for x in lista:
#     print(x)