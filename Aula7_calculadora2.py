class calculadora:

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def mutiplicacao(self, valor_a, valorb):
        return valor_a * valor_b

    def divisao(self, valor_a, valorb):
        return valor_a / valor_b


calculadora = calculadora()
print(calculadora.soma(10, 2))
print(calculadora.subtracao(5, 3))
print(calculadora.divisao(100, 2))
print(calculadora.mutiplicacao(10, 5))