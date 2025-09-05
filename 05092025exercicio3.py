def criar_usuario():
    while True:
        usuario = input("Digite o nome de usuário: ").strip()
        senha = input("Digite a senha: ").strip()

        # Verifica se a senha é igual ou contém o usuário
        if senha == usuario:
            print("❌ Erro: a senha não pode ser igual ao nome de usuário.")
        elif usuario.lower() in senha.lower():
            print("❌ Erro: a senha não pode conter o nome de usuário.")
        else:
            print("✅ Usuário e senha cadastrados com sucesso!")
            break

if __name__ == "__main__":
    criar_usuario()
