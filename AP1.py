"""
AP1 PROGRAMAÇÃO ESTRUTURADA
Integrantes: Bryan Amorin, Jeronimo Chiclana, Julia Siodaro

"""
import random

# Operações do aventureiro
def aventureiro_andar(aventureiro, direcao):

    if direcao == "W":
        if aventureiro["posicao"][-1] == 0:
            return False
        else:
            aventureiro["posicao"][-1] -= 1
            return True
    elif direcao == "A":
        if aventureiro["posicao"][0] == 0:
            return False
        else:
            aventureiro["posicao"][0] -= 1
            return True
    elif direcao == "S":
        if aventureiro["posicao"][-1] == 9:
            return False
        else:
            aventureiro["posicao"][-1] += 1
            return True
    elif direcao == "D":
        if aventureiro["posicao"][0] == 9:
            return False
        else:
            aventureiro["posicao"][0] += 1
            return True
    else:
        return False

def aventureiro_atacar(aventureiro):

    forca = aventureiro["forca"] + random.randint(1, 6)
    return forca

def aventureiro_defender(aventureiro, dano):

    damage = dano - aventureiro["defesa"]
    if damage < 0:
        damage = 0

    aventureiro["vida"] -= damage

def ver_atributos_aventureiro(aventureiro):

    for chave, valor in aventureiro.items():
        print(f"{chave}: {valor}")

def aventureiro_esta_vivo(aventureiro):

    return aventureiro["vida"] > 0

# Operações do monstro
def novo_monstro():

    monstro = {
        "forca": random.randint(5, 25),
        "vida": random.randint(10, 100),
    }
    print("Um novo monstro apareceu!")
    print("-"*30)
    return monstro

def monstro_atacar(monstro):

    dano = monstro["forca"]
    return dano

def monstro_defender(monstro, dano):

    monstro["vida"] -= dano

def monstro_esta_vivo(monstro):

    return monstro["vida"] > 0

# Operações do mapa
def desenhar(aventureiro, tesouro):

    for y in range(10):
        for x in range(10):
            if [x, y] == aventureiro["posicao"]:
                print("@", end=" ")
            elif [x, y] == tesouro:
                print("X", end=" ")
            else:
                print(".", end=" ")
        print()

# Combate
def iniciar_combate(aventureiro, monstro):

    rodada = 0
    while rodada < 1000:
        rodada += 1
        print("Rodada ", rodada)
        print("Vida do Monstro:", monstro["vida"])
        print("Vida do Aventureiro:", aventureiro["vida"])
        print("-"*30)


        dano_aventureiro = aventureiro_atacar(aventureiro)
        monstro_defender(monstro, dano_aventureiro)
        print("Ataque do Aventureiro!")
        print("Dano causado:", dano_aventureiro)
        if monstro["vida"] < 0:
            print("Vida atual do monstro: 0")
        else:
            print("Vida atual do monstro:", monstro['vida'])
        print("-"*30)

        if not monstro_esta_vivo(monstro):
            print("Monstro perdeu!")
            print("Vida do Aventureiro:", aventureiro["vida"])
            return True

        dano_monstro = monstro_atacar(monstro)
        aventureiro_defender(aventureiro, dano_monstro)
        print("Ataque do Monstro!")
        print("Dano causado:", dano_monstro)
        print("Defesa do Aventureiro:", aventureiro["defesa"])
        print("Vida do Aventureiro:", aventureiro["vida"])
        print("-"*30)

        if not aventureiro_esta_vivo(aventureiro):
            print("Aventureiro perdeu!")
            return False

# Operação principal do jogo
def movimentar(aventureiro, direcao):

    if not aventureiro_andar(aventureiro, direcao):
        return True

    efeito = random.choices(["nada", "monstro"], [0.6, 0.4])[0]
    if efeito == "monstro":
        monstro = novo_monstro()
        return iniciar_combate(aventureiro, monstro)

    return True

def gerar_tesouro():

    x, y = 0, 0
    while (x, y) == (0, 0):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    return [x, y]

def main():

    aventureiro = {
        "forca": random.randint(10, 18),
        "defesa": random.randint(10, 18),
        "vida": random.randint(100, 120),
        "posicao": [0, 0]
    }

    tesouro = gerar_tesouro()

    aventureiro["nome"] = input("Deseja buscar um tesouro? Primeiro, informe seu nome: ")
    print(f"Saudações, {aventureiro['nome']}! Boa sorte!")

    desenhar(aventureiro, tesouro)

    while True:
        op = input("Insira o seu comando: ").upper()
        if op == "Q":
            print("Já correndo?")
            break
        elif op == "T":
            ver_atributos_aventureiro(aventureiro)
        elif op in ["W", "A", "S", "D"]:
            if movimentar(aventureiro, op):
                desenhar(aventureiro, tesouro)
            else:
                print("Game Over...")
                break
        else:
            print(f"{aventureiro['nome']}, não conheço essa opção! Tente novamente!")

        if aventureiro["posicao"] == tesouro:
            print(f"Parabéns, {aventureiro['nome']}! Você encontrou o tesouro!")
            break

if __name__ == "__main__":
    main()
