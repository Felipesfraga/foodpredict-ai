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
        pergunta = input("Deseja cadastrar o primeiro dia de pedidos? (y/n): ").lower().strip()
    else:
        pergunta = input(f"Deseja cadastrar o dia {total_dias +1} de pedidos? (y/n): ").lower().strip()



    # Fluxo A: Cliente quer encerrar e ver os resultados
    if pergunta == "n":
        #Validação de crash: o cliente não pode sair sem ter pelo menos adicionado 1 dia
        if total_dias == 0:
            print("⚠ Atenção: você precisa cadastrar pelo menos 1 dia para calcular a média!\n")
            continue      # <--- Aqui o python pega o cursor da onde a gênte tá e joga para lá no começo do While True.

        break             # <--- Só lé quando a lista não estiver vazia ai ele sai do loop e vai para o código a baixo

    
    # Fluxo B: Cliente quer cadastrar dados
    if pergunta == "y":
        try:              #<--- Gaiola de proteção em caso escrever (abc) ele trava e evita de crashar e vai para o "except"
            novo_pedido = int(input(f"Digite a quantidade de pedidos do dia {total_dias +1}: "))

            if novo_pedido <0:
                print("❌ Erro: Não são aceitos números negativos. Digite um valor válido.\n")

            else:
                pedidos.append(novo_pedido)
                print(f"✅ Sucesso: Dia {total_dias +1} cadastrado!\n")

        except ValueError:
            print("❌ Erro: Entrada inválida! Por favor digite apenas números inteiros.\n")

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

#4. Exibir variação entre os dias consecultivos (funciona só se tiver 2 dias ou mais).
# if len() evita de mostrar um relatório com a seção vazia.
if len(pedidos) > 1:
    print("\n---------------------------------------------------------")
    print("              ANÁLISE DE VARIAÇÃO DIÁRIA                   ")
    print("---------------------------------------------------------")

    # Criei 3 contadores zerados antes do 'for' começar e ir adicionando. (se tiver dentro ele zera toda vez que compara)
    qtd_crescimento = 0
    qtd_queda = 0 
    qtd_estavel = 0

    # O range começa em indice 1 porque é no segundo dia e vai até o total da lista
    for i in range(1, len(pedidos)):
        dia_atual = pedidos[i]
        dia_anterior = pedidos[i - 1]
        

        # O 'i' é o indice do python(1, 2, 3...), e soma +1 que mostra o dia do cliente
        if dia_atual > dia_anterior:
            diferenca = dia_atual - dia_anterior
            print(f"📈 Dia {i} para Dia {i + 1}: Crescimento | (+{diferenca} pedidos)")
            
            qtd_crescimento +=1               # <--- Soma +1 no contador de crescimento

        elif dia_atual  < dia_anterior:
            diferenca = dia_anterior - dia_atual
            print(f"📉 Dia {i} para Dia {i + 1}: Queda       | (-{diferenca} pedidos)")
            
            qtd_queda += 1                   # <--- Soma +1 no contador de queda

        else:
            print(f"➖ Dia {i} para Dia {i + 1}: Estável     | ( 0 variação)")

            qtd_estavel += 1                 # <--- Soma +1 no contador de estavel

    # Exibir placar final (alinhado com ele)
    print("\n---------- Resumo das Variações Diárias ----------")
    print(f"📈 Total de Intervalos em crescimento: {qtd_crescimento}")
    print(f"📉 Total de Intervalos em queda:       {qtd_queda}")
    print(f"➖ Total de Intervalos estaveis:       {qtd_estavel}")

else:
        print("\n❗ Cadastre pelo menos 2 dias para visualizar a tendência de variação.")
            

print("\n=========================================================")
print("     Obrigado por usar o FoodPredict AI Até a próxima.      ")
print("===========================================================")