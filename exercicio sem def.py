""""
Dada uma lista de palavras, escreva um programa que solicite
ao usuario uma  lista de frutas e mostre:
- A lista original
- A lista ordenada
- A lista na ordem inversa

"""
import os
os.system("cls || clear")

lista_frutas = []

# Entrada.
print("=== Solicitando a lista de frutas para o Usuario ===")
while True:
    nome = input("Digite As Frutas para fazer a Lista: ")
    if nome.lower() == "sair":
        break
    else:
        lista_frutas.append(nome)

# Processamento
print("\nOrdenando lista...")
lista_original = sorted(lista_frutas)

print("\nOrdenando lista...")
lista_ordenada = sorted(lista_frutas)

print("\nOrdenando lista...")
lista_ordem_inversa = sorted(lista_frutas, reverse=True)
print("Lista invertida:", lista_ordem_inversa)

# Saida
print("\n=== Resultado ===")
print("Lista original:")
print(lista_frutas)

print("\nLista ordenada:")
print(lista_ordenada)

print("\nLista ordem inversa:")
print(lista_ordem_inversa)


