""""
Dada uma lista de palavras, escreva um programa que solicite
ao usuario uma  lista de frutas e mostre:
- A lista original
- A lista ordenada
- A lista na ordem inversa

"""
import os
os.system("cls || clear")


# Entrada
def ordenar_frutas():
  
  frutas = input("Digite uma lista de frutas separadas por vírgula: ").split(',')

  print("Lista original:", frutas)

# Processamento
  frutas_ordenadas = sorted(frutas)
  print("Lista ordenada:", frutas_ordenadas)

  frutas_inversas = sorted(frutas, reverse=True)
  print("Lista invertida:", frutas_inversas)

# Saida  
if __name__ == "__main__":
  ordenar_frutas()
