def formulario():
    # Nome: mínimo 4 caracteres
    while True:
        nome = input("Digite seu nome (mínimo 4 caracteres): ").strip()
        if len(nome) >= 4:
            break
        else:
            print("❌ Erro: o nome deve ter pelo menos 4 caracteres.")

    # Idade: entre 1 e 100
    while True:
        try:
            idade = int(input("Digite sua idade (1 a 100): "))
            if 1 <= idade <= 100:
                break
            else:
                print("❌ Erro: idade deve estar entre 1 e 100.")
        except ValueError:
            print("❌ Erro: digite um número inteiro válido.")

    # Salário: valor positivo
    while True:
        try:
            salario = float(input("Digite seu salário (valor positivo): "))
            if salario > 0:
                break
            else:
                print("❌ Erro: o salário deve ser maior que zero.")
        except ValueError:
            print("❌ Erro: digite um número válido.")

    # Gênero: f, m ou o
    while True:
        genero = input("Digite seu gênero (f - feminino, m - masculino, o - outro): ").lower().strip()
        if genero in ['f', 'm', 'o']:
            break
        else:
            print("❌ Erro: gênero inválido. Digite 'f', 'm' ou 'o'.")

    # Situação Empregatícia: e, d ou a
    while True:
        situacao = input("Digite sua situação empregatícia (e - empregado, d - desempregado, a - autônomo): ").lower().strip()
        if situacao in ['e', 'd', 'a']:
            break
        else:
            print("❌ Erro: situação inválida. Digite 'e', 'd' ou 'a'.")

    # Exibir dados validados
    print("\n✅ Dados cadastrados com sucesso:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: R$ {salario:.2f}")
    print(f"Gênero: {genero}")
    print(f"Situação Empregatícia: {situacao}")

formulario()
