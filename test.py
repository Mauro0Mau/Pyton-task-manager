import time
import os

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
print(pessoa ["idade"])
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

print(mauricio["amigos"]["evelyn"]["idade"])
print(mauricio["amigos"]["evelyn"]["status"])
print(mauricio["amigos"]["evelyn"]["relacionamento"])
print(mauricio["amigos"]["evelyn"]["personalidade"])