def informacoes_criatura():
    nome = input()
    vida = int(input())
    nivel = int(input())
    return nome, (vida, nivel)

def ord_nivel(criatura):
    return criatura[1][1]

def main():
    criaturas = []

    for _ in range(3):
        nome, stats = informacoes_criatura()
        criaturas.append([nome, stats])

    print(criaturas)

    criaturas_ordem = sorted(criaturas, key=ord_nivel, reverse=True)
    for criatura in criaturas_ordem:
        print(criatura[0])

if __name__ == "__main__":
    main()