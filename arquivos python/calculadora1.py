 # -*- coding: utf-8 -*-
"""
CALCULADORA
Autor: Maycon Gentil
Função: Soma, Divisão, Multiplicação, Subtração
"""
print (" -----------Calculadora v2.0--------------- ")

sair = False

while sair == False:
  num1 = input("Digite o primeiro número: ")
  num1 = int(num1)
  operador = input("Digite o operador: + - / * ")
  num2 = input("Digite o segundo número: ")
  num2 = int(num2)

  #SOMA +
  if operador == "+":
      operacao = num1 + num2
  #DIVISÃO /
  if operador == "/":
      operacao = num1 / num2
  #MULTIPLICACAO *
  if operador == "*":
      operacao = num1 * num2
  #SUBTRACAO -
  if operador == "-":
      operacao = num1 - num2

  print ("Resultado: ")
  print (operacao)
  
  teste = input("Deseja Sair? S ou N?:")
  if teste  == "S":
    sair = True