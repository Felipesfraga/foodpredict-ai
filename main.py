pedidos = [10, 20, 30]

# adicionar mais 1 dia manualmente
pergunta = input("Deseja adicionar mais um dia a lista de pedidos? (y/n): ")

# se for "y" ele adiciona mais 1 dia manualmente
if pergunta == "y":
  novo_pedido = int(input("Digite o pedido do dia: "))
  pedidos.append(novo_pedido)
print("")
# se for "n" (ou qualquer outro), ele ignora o if
print("FoodPredict AI")

media = sum(pedidos) / len(pedidos)

print("Histórico de pedidos de cada dia:", pedidos)

print("Média de pedidos por dia:",media)