import time
import os

'''
nome = "Mauricio"

print ("Esse cara é O cara: " + nome)

x = 25
y = 25
z = 25

print  (x + y)
print  (x - z)
print  (x * y)
print  (x / z)

a = 1 + 129
d = - 130 
c = a + d
b = c + d

print (b)
        
m = 18

if m == 18:
    print(b)
else:
    print(m)

for i in range(1, 11):
    time.sleep(0.5)
    print(i)
    if i == 5:
        break

print("\n")

limite = 0

while limite < 11:
    print(limite)
    time.sleep(0.1)
    limite +=1

def wellcome (nome):
    print(f"Bem vindo {nome}")

wellcome("Mauricio")

cores = ["azul", "vermelho", "verde", "amarelo"]
for cor in cores:
    print(cor)

print("\n")

pessoa = {
    "nome": "Mauricio",
    "idade": 25,
    "sexo": "M"
}

print(pessoa ["nome"])
time.sleep(0.1)
print(pessoa ["idade"])
time.sleep(0.1)
print(pessoa ["sexo"])


test_path = r"D:\Estudos de Programação\Pyton\teste"
caminho_index = os.path.join(test_path, "index.html")
caminho_style = os.path.join(test_path, "style.css")
caminho_arquivo = os.path.join(test_path, "arquivo.txt")

# Criando a pasta caso não exista
os.makedirs(test_path, exist_ok=True)

# Abrindo e escrevendo no arquivo
with open(caminho_index, "w") as index:
    index.write("<!DOCTYPE html>")
    index.write("\n<html>")
    index.write("\n<head>")
    index.write("\n<title>Teste</title>")
    index.write(f"\n<link rel='stylesheet' type='text/css' href='../teste/style.css'>")#Linkando o CSS
    index.write("\n</head>")
    index.write("\n<body>")
    index.write("\n<h1>Teste</h1>")
    index.write("\n<h2>Teste2</h2>")
    index.write("\n<h3>Teste3</h3>")
    index.write("\n</body>")
    index.write("\n</html>")
    
# Criando e escrevendo no arquivo CSS
with open(caminho_style, "w") as css:
    css.write("h1 { color: red; }")  # Exemplo de estilo
    css.write("\nh2 { color: blue; }")
    css.write("\nh3 { color: green; }")

with open(caminho_arquivo, "w") as arquivo:
    arquivo.write("Teste de arquivo")

try:
    resultado = 10 / 10
except ZeroDivisionError:
    print("Não é possível dividir por zero")
else:
    print(resultado)

mauricio = {
    "idade": 7,
    "dinheiro": "R$" + str(125),
    "mae": "Joyce",
    "pai": {
        "nome": "Dênis",
        "dinheiro": "R$" + str(400),
    },
    "familia": {
        "vo": {
            "nome": "Sebastião",
            "relação": "Amistosa, não apoia aquilo que não conhece como decisões minhas ou de outros que ele já tenha um pré-conceito com o indivíduo",
            "idade": None,
        },
        "voa": "Aparecida",
    },
    "amigos": {
        "evelyn": {
            "idade": 18, 
            "status": "Incrível" + " confiável",
            "relacionamento": "Fora de cogitação",
            "personalidade": "Gentil e carismática",
        },
        "default": {
            "idade": None,
            "status": None,
            "relacionamento": None,
            "personalidade": None,
            "endereco": ["Rua", "Bairro", "Cidade", "Estado"],
        },
    },
    "comida_fav": {
        "risoto_salmao": {
            "ingrediente": {
                "arroz": str(200) + "g",
                "cebola": "1/4",
                "colher": "1" + "Sopa de margarina",
                "sal-pimenta": "a gosto",
            }
        }
    }
}

time.sleep(0.1)
print(mauricio["amigos"]["evelyn"]["idade"])
time.sleep(0.1)
print(mauricio["amigos"]["evelyn"]["status"])
time.sleep(0.1)
print(mauricio["amigos"]["evelyn"]["relacionamento"])
time.sleep(0.1)
print(mauricio["amigos"]["evelyn"]["personalidade"])


nameSTU = 'Stu'

print(type(nameSTU))

lista1 = [1, 2, 3, 4, 5, 6]
print (lista1[2])

time.sleep(1)
lista1.append(6) #Adiciona um item na lista
print(lista1)

time.sleep(1)
lista1.pop() #Remove o último item da lista
print(lista1)

time.sleep(1)
lista1.pop(0) #Remove o item na posição 0
print(lista1)

time.sleep(1)
lista1.remove(3) #Remove o item 3 da lista
print(lista1)

time.sleep(1)
lista1.sort() #Ordena a lista
print(lista1)

AB, CD, ACDC = [1, 2, 3 + 2]
print(ACDC)

listaTsom = [1, 2, 3, 2 + 2, 5, 12/2, 3.5 + 3.5, 80, 9, 10]
listaTsom2 = [11, 12, 13, 14, 15]

lista_Somada = listaTsom + listaTsom2
print(lista_Somada)

tupla = (1, 2, 3, 4)
print(tupla[3])
'''

'''
a = 10
b = 5

print("\n".join(map(str, [a + b, a - b, a * b, a / b])))

time.sleep(0.5)

operacoes = [a + b, a - b, a * b, a / b]

for resultado in operacoes:
    print('\n')          
    print(resultado)
    time.sleep(0.1) 
'''


#-------------------------------------------- Praticas --------------------------------------------


print("Olá, Temos um tempo para que essa execução acabe começando agora")
time.sleep(1)
print("1")
time.sleep(1)
print("2")
time.sleep(1)
print("3")
time.sleep(1)
print("4")
time.sleep(1)
print("5")

print("\n")

print ("Començando por algumas operações básicas de aritmética:")
time.sleep(0.5)

a = 10
b = 5

print (a + b)
time.sleep(0.1)
print (a - b)
time.sleep(0.1)
print (a * b)
time.sleep(0.1)
print (a / b)

nomeA = 'Gabrielly'

if nomeA == 'Gabrielly':
    print("O nome é... " + nomeA + "?")
else:
    print("O nome não é Gabrielly")

for i in range(1, 11):
    print(i)

contador = 0

while contador < 11:
    print(contador)
    contador += 1

def bemvindo (nome):
    print(f"Bem vindo {nome}")
    bemvindo("Gabrielly")

cores = ["azul", "vermelho", "verde", "amarelo"]
for cor in cores:
    print(cor)

print("\n")

pessoa = {
    "nome": "Gabrielly",
    "idade": 18,
    "sexo": "F"
}

camiho_teste = r"D:\Estudos de Programação\Pyton\teste"
caminho_arquivo = os.path.join(camiho_teste, "arquivo.txt")

with open(caminho_arquivo, "w") as arquivo:
    arquivo.write("Teste de arquivo" + ", Olá Mundo!")

try:
    resultado = 10 / 10
    print (resultado)
except ZeroDivisionError:
    print("Não é possível dividir por zero")

variavel = 10
print(type(variavel))

lista = [1, 2, 3, 4, 5, 6]
print(lista[2])

lista[1] = 'GOOFY'
print(lista[1])
print(lista)

lista.append(7)
print(lista)

lista.remove('GOOFY', 7)
print(lista)

lista.sort()
print(lista)

x, y, z = [1, 2, 3]
print(x, y, z)

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
listamain = lista1 + lista2
print(listamain)

tupla = (1, 2, 3, 4)
print(tupla[3])

ele = {
    "nome": ["Nelço", "Gloria"],
    "idade": 102,
    "sexo": ["M", "F"]
}

print(ele["nome"])

def soma (a, b):
    return a + b

resultado = soma(10, 5)
print(resultado)

def quadrado (x):
    return x ** 2
print(quadrado(4))

def saudacoes (nomeB = "Visitante"):
    print(f"Olá {nomeB}!")

saudacoes("Ana")
saudacoes()

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    print(fatorial(5))

soma = lambda a, b: a + b
print(soma(10, 5))

quadrados = [x ** 2 for x in range(6)]
print(quadrados)

numeros = [1, 2, 3, 4]
quadrado = list(map(lambda x: x ** 2, numeros))
print(quadrado)

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

from functools import reduce
soma_total= reduce(lambda a, b: a + b, numeros)
print(soma_total)

dicionario = {x: x ** 2 for x in range(5)}
print(dicionario)





