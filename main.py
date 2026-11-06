pedidos = [10, 20, 30]

print("========== Cadastros de pedidos (FoodPredict AI) ==========")

#com while ele adiciona o dia varias vezes
# se for "y" ele adiciona mais 1 dia manualmente
# .lower() serve para que no final mesmo se a pessoas colocar maiusculo, vai ficar minusculo

while True:
    # adicionar mais 1 dia manualmente
    pergunta = input("Deseja adicionar mais um dia a lista de pedidos? (y/n): ").lower()


    #se a resposta for 'n', o 'break' quebra o while e sai do laço

    if pergunta == "n":
        break

    if pergunta == "y":
        novo_pedido = int(input("Digite a quantidade de pedidos no dia: "))
        pedidos.append(novo_pedido)
        print("")

    else:
        #caso digite qualquer outra entrada
        print("===Opção inválida! Digite apenas 'y' ou 'n'.===\n")

print("\n" + "="*50)
print("FoodPredict AI - RESULTADOS\n")

media = round(sum(pedidos) / len(pedidos), 2)

print("Histórico de pedidos de cada dia:", pedidos)

print("Média de pedidos por dia:", media)