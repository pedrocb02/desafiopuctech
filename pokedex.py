import json
import os


try:
    with open("pokedex.json", "r") as f:
        pokemons = json.load(f)
except FileNotFoundError:
    pokemons = []
    with open("pokedex.json", "w") as f:
        json.dump(pokemons, f, indent=4)

def pokemon_duplicado(nome, lista_pokemons):
    for p in lista_pokemons:
        if p["nome"].strip().lower() == nome.strip().lower():
            return True
    return False

def adicionar_pokemon(nome, tipo, nivel):
    if not nome or not nome.strip():
        print("Nome não pode ser vazio!")
        return

    with open("pokedex.json", "r") as f:
        pokemons = json.load(f)

    if pokemon_duplicado(nome, pokemons):
        print(f"Erro: O Pokémon '{nome}' já está registrado na sua Pokédex!")
        return
   
    if len(pokemons) == 0:
        novo_id = 1
    else:
        novo_id = pokemons[-1]["id"] + 1

    novo_pokemon = {
        "id": novo_id,
        "nome": nome,
        "tipo": tipo,
        "nivel": nivel
    }
    
    pokemons.append(novo_pokemon)
    
    with open("pokedex.json", "w") as f:
        json.dump(pokemons, f, indent=4)
        
    print(f"Pokémon '{nome}' adicionado com sucesso!")

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
        
def atualizar_pokemon(ID, novo_nome, novo_tipo, novo_nivel):
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
    else:
        with open("pokedex.json", "w") as f:
            json.dump(pokemons, f, indent=4)
        print("Pokémon atualizado com sucesso!")

def limpar_terminal():
    try:
        from IPython.display import clear_output
        clear_output(wait=True)
    except ImportError:
        os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("Pressione Enter para continuar...")

def main():
    while True:
        print("\n--- Menu ---")
        print("[1] Adicionar Pokémon")
        print("[2] Listar Pokémons")
        print("[3] Editar Pokémon")
        print("[4] Remover Pokémon")
        print("[5] Sair")

        escolha = input("Escolha a opção desejada: ")

        if escolha == "1":
            try:
                nome = input("Digite o nome do Pokémon: ").strip()
                tipo = input("Digite o tipo do Pokémon: ").strip()
                nivel = int(input("Digite o nível do Pokémon: "))
                adicionar_pokemon(nome, tipo, nivel)
            except ValueError:
                print("Erro: O nível precisa ser um número inteiro.")
            pausar()
            limpar_terminal()

        elif escolha == "2":
            listar_pokemons()
            pausar()
            limpar_terminal()

        elif escolha == "3":
            try:
                id_busca = input("Digite o ID do Pokémon que deseja atualizar: ").strip()
                novo_nome = input("Digite o novo nome: ").strip()
                novo_tipo = input("Digite o novo tipo: ").strip()
                novo_nivel = int(input("Digite o novo nível: "))
                atualizar_pokemon(id_busca, novo_nome, novo_tipo, novo_nivel)
            except ValueError:
                print("Erro: O nível precisa ser um número inteiro válido.")
            pausar()
            limpar_terminal()

        elif escolha == "4":
            id_remover = input("Digite o ID do Pokémon que deseja remover: ").strip()
            remover_pokemon(id_remover)
            pausar()
            limpar_terminal()

        elif escolha == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")
            pausar()
            limpar_terminal()

if __name__ == "__main__":
    main()