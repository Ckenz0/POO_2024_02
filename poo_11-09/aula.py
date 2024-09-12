#metodo antigo
#f = open("teste.txt", "w", encoding="utf-8")
#f.write("onde esta a ")
#f.close()

#metodo novo
#escrita em arquivo
with open("poo_11-09/teste.txt", "w", encoding="utf-8") as f:
    f.write("hmmmmmmmmmmmmmmmmmmmmmm\n")
    f.write("VAMOS POR PARTES QUE NEM O JACK")

#leitura em arquivo
with open("poo_11-09/teste.txt", "r", encoding="utf-8") as f:
    conteudo = f.read()
    print(conteudo)
print("BRUNAO COMO O BOI FAZ?")

#Leitura em uma linha
with open("poo_11-09/teste.txt", "r", encoding="utf-8") as f:
    linha = f.readline()
    print(linha)

#Leitura em uma linha 2
with open("poo_11-09/teste.txt", "r", encoding="utf-8") as f:
    for linha in f.readlines():
        print(linha + "\nfoquinha")
        
#ler quantidade bytes
with open("poo_11-09/teste.txt", "r", encoding="utf-8") as f:
    ##conteudo = f.read(1024)
    conteudo = f.read()[5:10]
    print(conteudo)

#posicionar o ponteiro do arquivo em uma posição
with open("poo_11-09/teste.txt", "r", encoding="utf-8") as f:
    f.seek(1)
    texto = f.readline()
    print("focao"+texto)

import pickle
dicionario = {"Nome": "Jack", "Idade": "HMMMMM NAO ABRIU", "CPF": "22Por partes22"}
#serializa o conteudo do dicionario
with open("poo_11-09/teste.pkl", "wb") as f:
    pickle.dump(dicionario, f)

with open("poo_11-09/teste.pkl", "rb") as f:
    dicionario_lido = pickle.load(f)
    print(dicionario_lido)

import json
with open("poo_11-09/teste.json", "w", encoding="utf-8") as f:
    json.dump(dicionario, f, indent = 4)

try:
    with open("poo_11-09/teste1.json", "r", encoding="utf-8") as f:
        mydic = json.load(f)
        print(mydic)
except FileNotFoundError as e:
    print(f"Ocorreu um erro: {e}")

