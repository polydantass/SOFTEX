def solicitar_nota(): 

    while True: 

        try: 

            nota = float(input("Digite uma nota entre 0 e 5: ")) 

            if 0 <= nota <= 5: 

                print(f"✅ Nota registrada com sucesso: {nota}") 

                break 

            else: 

                print("❌ Erro: a nota deve estar entre 0 e 5.") 

        except ValueError: 

            print("❌ Erro: digite um número válido.") 

 
 

solicitar_nota() 

