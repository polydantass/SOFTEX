# Sistema de Bilheteria de Cinema - Versão US3  

print("=" * 40)  
print(" 🎬 Bem-vindo ao Cinema Aurora 🎬 ")  
print("=" * 40)  

total_ingressos = 0  
total_arrecadado = 0  

continuar = "s"  

while continuar.lower() == "s":  
    idade = int(input("\nDigite a idade do cliente: "))  

    if idade < 12:  
        preco = 15.00  
        print(f"➡️ Ingresso Infantil: R$ {preco:.2f}")  

    else:  
        estudante = input("O cliente é estudante? (s/n): ").lower()  

        if estudante == "s":  
            preco = 15.00  
            print(f"➡️ Ingresso Meia-entrada (Estudante): R$ {preco:.2f}")  
        else:  
            preco = 30.00  
            print(f"➡️ Ingresso Inteira: R$ {preco:.2f}")  

    total_ingressos += 1  
    total_arrecadado += preco  

    continuar = input("\nDeseja registrar um novo cliente? (s/n): ")  

print("\n" + "=" * 40)  
print("📢 Fim do expediente.")  
print(f"🎟️ Total de ingressos vendidos: {total_ingressos}")  
print(f"💰 Valor total arrecadado: R$ {total_arrecadado:.2f}")  
print("🍿 Obrigado pela preferência! Até a próxima sessão! 🎥")  
print("=" * 40)  