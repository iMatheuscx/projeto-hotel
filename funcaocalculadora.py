# -*- coding: utf-8 -*-
"""funcaoCalculadora.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QIYRZ_BBZKgnyUnIDWMRFxapOIYEYA7J
"""

def calculadora(num1, num2, operacao):
   if operacao == 1:
      return num1 + num2
   elif operacao == 2:
     return num1 - num2
   elif operacao == 3:
     return num1 * num2
   elif operacao == 4:
      if num2 != 0:
         return num1 / num2
      else:
        return "Impossível dividir por zero"
   else:
      return 0

# Códigos das operações: soma = 1, subtração = 2, multiplicação = 3, divisão = 4
# Exemplos:
resultado = calculadora(6, 2, 1)
print("Resultado: ", resultado)

resultado = calculadora(10, 4, 2)
print("Resultado: ", resultado)

resultado = calculadora(3, 5, 3)
print("Resultado: ", resultado)

resultado = calculadora(7, 0, 4)
print("Resultado: ", resultado)

resultado = calculadora(9, 2, 4)
print("Resultado: ", resultado)