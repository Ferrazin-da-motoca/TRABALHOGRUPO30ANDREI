def uniao(conjunto1, conjunto2):
    return conjunto1.union(conjunto2)

def intersecao(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2)

def diferenca(conjunto1, conjunto2):
    return conjunto1.difference(conjunto2)

def produto_cartesiano(conjunto1, conjunto2):
    return {(x, y) for x in conjunto1 for y in conjunto2}

def main():
    while True:
        print("\nOperações disponíveis:")
        print("1 - União")
        print("2 - Interseção")
        print("3 - Diferença")
        print("4 - Produto Cartesiano")
        print("5 - Sair")

        escolha = input("Escolha uma das operação (-1-)(-2-)(-3-)(-4-)(-5-): ")

        if escolha == '5':
            break

        conjunto1 = set(input("Digite o primeiro conjunto, separando as opçoes usando espaço: ").split())
        conjunto2 = set(input("Digite o segundo conjunto, separando as opçoes usando espaço: ").split())

        resultado = set()

        if escolha == '1':
            resultado = uniao(conjunto1, conjunto2)
        elif escolha == '2':
            resultado = intersecao(conjunto1, conjunto2)
        elif escolha == '3':
            resultado = diferenca(conjunto1, conjunto2)
        elif escolha == '4':
            resultado = produto_cartesiano(conjunto1, conjunto2)
        else:
            print("Essa escolha não esta disponivel, escolha uma das 5.")
            continue

        print("Resultado:", resultado)


if __name__ == "__main__":
    main()
