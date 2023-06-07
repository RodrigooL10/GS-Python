def verificar_condicoes(temperatura, luminosidade, umidade):
    sugestoes = []

    if temperatura < 20 or temperatura > 30:
        sugestoes.append("ALERTA! A temperatura está fora da faixa ideal. Recomenda-se ajustar a temperatura.")
    else:
        sugestoes.append("A temperatura está dentro da faixa ideal")

    if luminosidade < 5000:
        sugestoes.append("ALERTA! A luminosidade está abaixo do ideal. Recomenda-se fornecer mais luz para as plantas.")
    else:
        sugestoes.append("A luminosidade está dentro da faixa ideal")

    if umidade < 60 or umidade > 80:
        sugestoes.append("ALERTA! A umidade está fora da faixa ideal. Recomenda-se ajustar a umidade.")
    else:
        sugestoes.append("A umidade está dentro da faixa ideal")

    return sugestoes


def coletar_dados_drones():
    num_drones = int(input("\nInsira a quantidade de drones: "))

    drones = []
    for i in range(num_drones):
        temperatura = float(input(f"\nInsira a temperatura do drone {i + 1}: "))
        luminosidade = float(input(f"Insira a luminosidade do drone {i + 1}: "))
        umidade = float(input(f"Insira a umidade do drone {i + 1}: "))

        drone = {"temperatura": temperatura, "luminosidade": luminosidade, "umidade": umidade}
        drones.append(drone)

    return drones

print("+-------------------------------------+")
print("|   Bem vindo ao projeto ThinkFarm!   |")
print("+-------------------------------------+")

# Coleta os dados dos drones
dados_drones = coletar_dados_drones()

print("\n--- Resultados e sugestões ---")

# Processa os dados de cada drone
for i, drone in enumerate(dados_drones):
    temperatura = drone["temperatura"]
    luminosidade = drone["luminosidade"]
    umidade = drone["umidade"]

    # Verifica as condições e obtém as sugestões
    sugestoes = verificar_condicoes(temperatura, luminosidade, umidade)

    # Imprime as sugestões para cada drone
    if sugestoes:
        num_drone = i + 1

        print(f"\nO drone {num_drone} está com:")
        print(f"Temperatura: {temperatura}, Luminosidade: {luminosidade} e umidade: {umidade}")
        print("Sugestões:")

        for sugestao in sugestoes:
            print(f"- {sugestao}")