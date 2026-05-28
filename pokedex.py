import json

#tenta abrir um arquivo e se nao conseguir cria um arquivo .json
try:
    with open("pokedex.json", "r") as f:
        pokemons = json.load(f)
except FileNotFoundError:
    pokemons = []

def adicionar_pokemon(nome, tipo, nivel):
    if not nome or not nome.strip():
        print("Nome não pode ser vazio!")
        return

    with open("pokedex.json", "r") as f:
        pokemons = json.load(f)
    
    if len(pokemons) == 0:
        novo_id = 1
    else:
        novo_id = pokemons[-1]["id"] + 1 #pega o ultimo ID da lista e soma 1

    novo_pokemon = {
        "id": novo_id,
        "nome": nome,
        "tipo": tipo,
        "nivel": nivel
    }
    
    pokemons.append(novo_pokemon)
    
    with open("pokedex.json", "w") as f:
        json.dump(pokemons, f, indent=4)

def listar_pokemons():
    with open("pokedex.json", "r") as f:
       pokemons = json.load(f)
    
    if len(pokemons) == 0:
        print("Pokedex vazia!")
    else:
        for i in pokemons:
            print(f"ID: {i['id']}, Nome: {i['nome']}, Tipo: {i['tipo']}, Nível: {i['nivel']}")
   
def remover_pokemon(ID):
    with open("pokedex.json", "r") as f:
        pokemons = json.load(f)

    tamanho_antes = len(pokemons)
    pokemons = [p for p in pokemons if int(p["id"]) != int(ID)]

    if len(pokemons) == tamanho_antes:
        print(f"Pokémon com ID {ID} não encontrado!")
    else:
        with open("pokedex.json", "w") as f:
            json.dump(pokemons, f, indent=4)
        print(f"Pokémon removido com sucesso!")
        
def atualizar_pokemon(ID,novo_nome,novo_tipo,novo_nivel):
    if not novo_nome or not novo_nome.strip():
        print("Nome não pode ser vazio!")
        return

    with open("pokedex.json", "r") as f:
        pokemons = json.load(f)
    
    
    encontrado = False
    for p in pokemons:
        if int(p["id"]) == int(ID):
            p["nome"] = novo_nome
            p["tipo"] = novo_tipo
            p["nivel"] = novo_nivel
            encontrado = True

    if not encontrado:
        print(f"Pokémon com ID {ID} não encontrado!")

    with open("pokedex.json", "w") as f:
        json.dump(pokemons, f, indent=4)

def buscar_por_nome(nome):
    with open("pokedex.json", "r") as f:
        pokemons = json.load(f)
    
    resultado = [p for p in pokemons if nome.lower() in p["nome"].lower()]
    
    if not resultado:
        print(f"Nenhum pokémon encontrado com o nome '{nome}'!")
    else:
        for p in resultado:
            print(f"ID: {p['id']}, Nome: {p['nome']}, Tipo: {p['tipo']}, Nível: {p['nivel']}")

#Buscar pokemons
def buscar_por_tipo(tipo):
    with open("pokedex.json", "r") as f:
        pokemons = json.load(f)
    
    resultado = [p for p in pokemons if p["tipo"].lower() == tipo.lower()]
    
    if not resultado:
        print(f"Nenhum pokémon do tipo '{tipo}' encontrado!")
    else:
        for p in resultado:
            print(f"ID: {p['id']}, Nome: {p['nome']}, Tipo: {p['tipo']}, Nível: {p['nivel']}")

def main():
    listar_pokemons()
    atualizar_pokemon(1, "Pikachu", "Eletrico", 100)
    listar_pokemons()
    remover_pokemon(1)
    listar_pokemons()

    adicionar_pokemon("Pikachu", "Eletrico", 35)
    adicionar_pokemon("Charmander", "Fogo", 10)
    buscar_por_nome("pika")
    buscar_por_tipo("Agua")

main()
