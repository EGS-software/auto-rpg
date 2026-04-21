def iniciar_rpg_manual():
    print("="*40)
    print("🎲 CALCULADORA DE D&D (DADOS MANUAIS) 🎲")
    print("="*40)

    while True:
        print("\nO que você quer calcular?")
        print("1 - ⚔️ Ataque")
        print("2 - 🛡️ Defesa (CA)")
        print("3 - 🔍 Procurar (Percepção)")
        print("4 - ❌ Sair")
        
        escolha = input("\nDigite o número: ")

        # --- OPÇÃO 1: ATAQUE ---
        if escolha == '1':
            print("\n--- CALCULANDO ATAQUE ---")
            # Agora você digita o valor do dado que rolou na mesa!
            dado = int(input("O que caiu no dado (d20)? ")) 
            modificador = int(input("Qual o seu modificador de atributo? "))
            proficiencia = int(input("Qual o seu bônus de proficiência? "))
            
            if dado == 20:
                print(f"👉 Resultado: Você tirou 20 no dado. ACERTO CRÍTICO! 💥 Dano dobrado!")
            elif dado == 1:
                print(f"👉 Resultado: Você tirou 1 no dado. FALHA CRÍTICA! 🤦‍♂️ Errou feio.")
            else:
                total = dado + modificador + proficiencia
                print(f"👉 Resultado: Dado ({dado}) + Modificador ({modificador}) + Proficiência ({proficiencia}) = TOTAL: {total}")

        # --- OPÇÃO 2: DEFESA ---
        elif escolha == '2':
            print("\n--- CALCULANDO DEFESA (CA) ---")
            print("Lembrando: Defesa não usa dado, é um valor fixo.")
            mod_destreza = int(input("Qual o seu modificador de Destreza? "))
            bonus_armadura = int(input("Qual o bônus da armadura/escudo? "))
            
            ca_total = 10 + mod_destreza + bonus_armadura
            print(f"👉 Resultado: Sua Classe de Armadura é {ca_total}. O inimigo precisa de {ca_total} ou mais para acertar!")

        # --- OPÇÃO 3: PROCURAR ---
        elif escolha == '3':
            print("\n--- TESTE DE PERCEPÇÃO ---")
            # Agora você digita o valor do dado que rolou na mesa!
            dado = int(input("O que caiu no dado (d20)? "))
            mod_sabedoria = int(input("Qual o seu modificador de Sabedoria? "))
            proficiencia = int(input("Qual o bônus de proficiência (digite 0 se não for treinado)? "))
            
            total = dado + mod_sabedoria + proficiencia
            print(f"👉 Resultado: Dado ({dado}) + Sabedoria ({mod_sabedoria}) + Proficiência ({proficiencia}) = TOTAL: {total}")

        # --- OPÇÃO 4: SAIR ---
        elif escolha == '4':
            print("\nEncerrando a calculadora... Boa caçada ao Espectro de Mil Faces! 👻")
            break
            
        else:
            print("\n⚠️ Opção inválida! Digite 1, 2, 3 ou 4.")

# Isso faz o programa começar
iniciar_rpg_manual()