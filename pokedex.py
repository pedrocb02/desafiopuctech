
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

    adicionar_pokemon = {
        "id": novo_id,
        "nome": nome,
        "tipo": tipo,
        "nivel": nivel
    }
    
    pokemons.append(adicionar_pokemon)
    
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

def main():
    while True:
        print("\n--- Menu ---")
        print("[1] Adicionar Pokémon")
        print("[2] Listar Pokémons")
        print("[3] atualizar_pokemon Nível de um Pokémon")
        print("[4] Remover Pokémon")
        print("[5] Sair")

        escolha = input("Escolha a opção desejada: ")

        if escolha == "1":
            adicionar_pokemon()

        elif escolha == "2":
            listar_pokemons()

        elif escolha == "3":
            try:
                nome_busca = input("Digite o nome do Pokémon que deseja atualizar_pokemon: ").strip()
                campo_para_atualizar_pokemon = "nivel"
                novo_valor = int(input("Digite o novo nível: "))
                atualizar_pokemon(nome_busca, campo_para_atualizar_pokemon, novo_valor)
            except ValueError:
                print("Erro: O nível precisa ser um número inteiro válido.")

        elif escolha == "4":
            nome_remover = input("Digite o nome do Pokémon que deseja remover: ").strip()
            remover(nome_remover)

        elif escolha == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
