# Hands On 1 - Investigação do Array
# Array com 10 temperaturas
def executar_hands_on_1(temperaturas):
    temperatura = []
    
    # 2. Mostrar todos os elementos
    print("\n--- TEMPERATURAS ---")
    for i in range(10):
        print(f"Índice {i}: {temperaturas[i]:.1f} °C")

    # 3. Inicializações
    soma = 0
    maior = temperaturas[0]
    menor = temperaturas[0]
    indice_maior = 0
    indice_menor = 0
    operacoes = 0

    # 4. Percorrer o array
    for i in range(10):
        soma += temperaturas[i]
        operacoes += 1

        # Verificar maior temperatura
        operacoes += 1
        if temperaturas[i] > maior:
            maior = temperaturas[i]
            indice_maior = i

        # Verificar menor temperatura
        operacoes += 1
        if temperaturas[i] < menor:
            menor = temperaturas[i]
            indice_menor = i

    # 5. Calcular a média
    media = soma / 10
    operacoes += 1
    # 6. Contar temperaturas acima da média
    acima_media = 0
    for i in range(10):
        operacoes += 1
        if temperaturas[i] > media:
            acima_media += 1

    # 7. Mostrar resultados
    print("\n--- RESULTADOS ---")
    print(f"Média: {media:.2f} °C")
    print(f"Maior temperatura: {maior:.1f} °C")
    print(f"Índice do maior valor: {indice_maior}")
    print(f"Menor temperatura: {menor:.1f} °C")
    print(f"Índice do menor valor: {indice_menor}")
    print(f"Quantidade de valores acima da média: {acima_media}")
    print(f"Total de operações realizadas: {operacoes}")

def executar_hands_on_2(sensores, limite):

    maior_temp = sensores[0][0]
    sensor_maior = 0
    horario_maior = 0
    soma_geral = 0
    acima_limite = 0
    media_sensor = [0.0] * 5  # média de cada sensor

    for i in range(5):
        soma_sensor = 0
        for j in range(24):
            temp = sensores[i][j]
            soma_sensor += temp          # soma do sensor
            soma_geral += temp           # soma geral

            print(f" Sensor {i} | Horário {j:02d}h: {temp:.2f}°C")

            if temp > maior_temp:
                maior_temp = temp
                sensor_maior = i
                horario_maior = j        # guarda índices
                
            if temp > limite:    
                acima_limite += 1        # conta acima do limite
                
        media_sensor[i] = soma_sensor / 24  # média do sensor

    media_geral = soma_geral / (5 * 24)


    print(f"Média geral: {media_geral:.2f}")
    print(f"Maior temperatura: {maior_temp:.2f}")
    print(f"Sensor: {sensor_maior}")
    print(f"Horário: {horario_maior}")
    print(f"Acima do limite ({limite}): {acima_limite}")