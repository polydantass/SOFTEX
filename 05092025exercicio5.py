def solicitar_valor_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("❌ Erro: o valor deve ser positivo.")
        except ValueError:
            print("❌ Erro: digite um número válido.")

def calcular_anos(pop_a, taxa_a, pop_b, taxa_b):
    anos = 0
    while pop_a <= pop_b:
        pop_a += pop_a * (taxa_a / 100)
        pop_b += pop_b * (taxa_b / 100)
        anos += 1
        # Evita loop infinito se taxa da A <= taxa da B
        if anos > 1000:
            return None
    return anos

while True:
    print("\n--- Crescimento de População ---")
    
    pop_a = solicitar_valor_positivo("Digite a população inicial da cidade A: ")
    taxa_a = solicitar_valor_positivo("Digite a taxa de crescimento anual (%) da cidade A: ")
    
    pop_b = solicitar_valor_positivo("Digite a população inicial da cidade B: ")
    taxa_b = solicitar_valor_positivo("Digite a taxa de crescimento anual (%) da cidade B: ")
    
    anos = calcular_anos(pop_a, taxa_a, pop_b, taxa_b)
    
    if anos is None:
        print("⚠️ A população da cidade A nunca ultrapassará a da cidade B com essas taxas.")
    else:
        print(f"✅ A população da cidade A ultrapassará a da cidade B em {anos} anos.")
    
    continuar = input("Deseja realizar outro cálculo? (s/n): ").lower()
    if continuar != 's':
        print("Até mais!")
        break

