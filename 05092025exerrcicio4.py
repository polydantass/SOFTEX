def calcular_anos():
    # Populações iniciais
    pop_a = 90000
    pop_b = 250000

    # Taxas de crescimento (em percentual)
    taxa_a = 3.5 / 100  # 3,5% -> 0,035
    taxa_b = 1.2 / 100  # 1,2% -> 0,012

    anos = 0  # contador de anos

    # Loop até população A >= população B
    while pop_a < pop_b:
        pop_a += pop_a * taxa_a  # crescimento da cidade A
        pop_b += pop_b * taxa_b  # crescimento da cidade B
        anos += 1

    print(f"Serão necessários {anos} anos para que a população da cidade A ultrapasse ou iguale a da cidade B.")
    print(f"População final da cidade A: {int(pop_a)}")
    print(f"População final da cidade B: {int(pop_b)}")

if __name__ == "__main__":
    calcular_anos()
