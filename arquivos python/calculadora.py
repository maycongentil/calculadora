# -*- coding: utf-8 -*-
"""
CALCULADORA
Autor: Maycon Gentil
Função: Soma, Divisão, Multiplicação, Subtração
"""
print (" -----------Calculadora v1.0--------------- ")

valor1 = input("Digite o primeiro número: ")
valor1 = int(valor1)
operador = input("Digite o operador: + - / * ")
valor2 = input("Digite o segundo número: ")
valor2 = int(valor2)

#SOMA +
if operador == "+":
    operacao = valor1 + valor2
#DIVISÃO /
if operador == "/":
    operacao = valor1 / valor2
#MULTIPLICACAO *
if operador == "*":
    operacao = valor1 * valor2
#SUBTRACAO -
if operador == "-":
    operacao = valor1 - valor2

print ("Resultado: ")
print (operacao)