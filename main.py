#1.Configurando um sistema de pedidos para um cliente deixando de forma mais amigavel ☻
pedidos = [] # lista com colchetes vazio para cadastrar pedidos do zero.

print("===========================================================")
print("                  CADASTROS DE PEDIDOS                     ")
print("                     Bem-vindo(a)                          ")
print("                   (FoodPredict AI)                        ")
print("===========================================================")
print("            Olá! Vamos organizar seus pedidos.             ")


#2. While True de laço de repetição continua para cadastrar os dias
while True:
    #len() mostra a todos pedidos separados em dias conforme acrescenta em mais pedidos.
    total_dias = len(pedidos)

    # Como lista está vazia, faz um if: de só uma pergunta para o primeiro dia e else: para os próximos dias. 
    #{total_dias +1} para ir adicionando todos os outros dias
    #.lower() transforma todos os caracteres de Maiusculos em minusculos
    # NOVIDADE: .strip() remove qualquer espaço se for adicionado
    if total_dias == 0:
        pergunta = input("Deseja cadastar o primeiro dia de pedidos? (y/n): ").lower().strip()
    else:
        pergunta = input(f"Deseja cadastar o dia {total_dias +1} de pedidos? (y/n): ").lower().strip()



    # Fluxo A: Cliente quer encerrar e ver os resultados
    if pergunta == "n":
        #Validação de crash: o cliente não pode sair sem ter pelo menos adicionado 1 dia
        if total_dias == 0:
            print("⚠ Atenção: você precisa cadastrar pelo menos 1 dia para calcular a média!\n")
            continue      # <--- Aqui o python pega o cursor da onde a gênte tá e joga para lá no começo do While True.

        break             # <--- Só lé quando a lista não estiver vazia ai ele sai do loop e vai para o código a baixo

    
    # Fluxo B: Cliente quer cadastar dados
    if pergunta == "y":
        try:              #<--- Gaiola de proteção em caso escrever (abc) ele trava e evita de crashar e vai para o "except"
            novo_pedido = int(input(f"Digite a quantidade de pedidos do dia {total_dias +1}: "))

            if novo_pedido <0:
                print("❌ Erro: Não são aceitos némros negativos. Digite um valor válido.\n")

            else:
                pedidos.append(novo_pedido)
                print(f"✅ Sucesso: Dia {total_dias +1} cadastrado!\n")

        except ValueError:
            print("❌ Erro: Entrada inválida! Por favor digite apenas némeros inteiros.\n")

    # Fluxo C: Cliente digitou qualquer outra coisa inválida
    else:
        print ("⚠ Opcão inválida! por favor, digite apenas 'y' para Sim ou 'n' para Não.\n")

#3. Tela de resultados Finais
print("===========================================================")
print("                    FoodPredict AI                         ")
print("                    SEUS RESULTADOS                        ")
print("===========================================================")

# Cálculo da média final com nmeros inteiros utilizando round
media = round(sum(pedidos) / len(pedidos), 2)

# Descobrindo os maiores e menores valores
maior_valor = max(pedidos)
menor_valor = min(pedidos)

# Cria uma lista vazia para quardar todos os dias que empatão no recorde
dias_maiores = []
dias_menores = []

# O enumerate() procura a lista e tenta achar os índices de todos os empates
#Se o valor de vairos dias for igual ao Maior/Menor valor histórico
for indice, valor in enumerate(pedidos):
    
    if valor == maior_valor:
        dias_maiores.append(indice +1)
        

    if valor == menor_valor:
        dias_menores.append(indice + 1)

print(f"📊 Total dos dias monitorados: {len(pedidos)} dias")
print(f"📈 Histórico de pedidos registrados: {pedidos}")
print(f"🌟 A sua média atual é de: {media} pedidos por dia")

# Exibir os recordes do dia para o cliente comun
print(f"🔥 Dia(s) com a maior quantidade de pedidos:  {dias_maiores} (com {maior_valor} pedidos)")
print(f"🧊 Dia(s) com a menor quantidade de pedidos:  {dias_menores} (com {menor_valor} pedidos)")

print("\n=========================================================")
print("     Obrigado por usar o FoodPredict AI Até a próxima.      ")
print("===========================================================")