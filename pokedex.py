import json
TIPOS_VALIDOS = [
    "Água", "Grama", "Fogo", "Elétrico", "Normal", "Voador",
    "Inseto", "Venenoso", "Terrestre", "Pedra", "Gelo",
    "Lutador", "Psíquico", "Fantasma", "Dragão", "Aço", "Sombrio", "Fada"
]

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
    if nivel < 1 or nivel > 100:
        print("Nivel deve ser entre 1 e 100!")
        return 
    if tipo not in TIPOS_VALIDOS:
        print("Tipo inexistente!")
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
    if novo_nivel < 1 or novo_nivel > 100:
        print("Nivel inválido")
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

def main():
    adicionar_pokemon("Squirtle", "Agua", -1)
    listar_pokemons()
    atualizar_pokemon(1, "Pikachu", "Eletrico", 101)
    listar_pokemons()
    remover_pokemon(1)
    listar_pokemons()

main()
