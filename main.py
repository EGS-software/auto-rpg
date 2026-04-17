import random

def iniciar_rpg():
    print("="*40)
    print("🎲 ROLADOR DE DADOS D&D AUTOMÁTICO 🎲")
    print("="*40)

    # Esse 'while True' faz o programa rodar para sempre, até você mandar sair!
    while True:
        print("\nO que você quer fazer?")
        print("1 - ⚔️ Atacar")
        print("2 - 🛡️ Calcular Defesa (CA)")
        print("3 - 🔍 Procurar (Percepção)")
        print("4 - ❌ Sair do programa")
        
        escolha = input("\nDigite o número da sua escolha: ")

        # --- OPÇÃO 1: ATAQUE ---
        if escolha == '1':
            print("\n--- ROLANDO ATAQUE ---")
            modificador = int(input("Qual o seu modificador de atributo (ex: Força ou Destreza)? "))
            proficiencia = int(input("Qual o seu bônus de proficiência? "))
            
            dado = random.randint(1, 20)
            
            if dado == 20:
                print(f"👉 Resultado: Você rolou {dado} no dado. ACERTO CRÍTICO! Dano dobrado!")
            elif dado == 1:
                print(f"👉 Resultado: Você rolou {dado} no dado. FALHA CRÍTICA! Você errou feio.")
            else:
                total = dado + modificador + proficiencia
                print(f"👉 Resultado: Dado ({dado}) + Modificador ({modificador}) + Proficiência ({proficiencia}) = TOTAL: {total}")

        # --- OPÇÃO 2: DEFESA ---
        elif escolha == '2':
            print("\n--- CALCULANDO DEFESA (CA) ---")
            print("Lembrando: A base natural é 10.")
            mod_destreza = int(input("Qual o seu modificador de Destreza? "))
            bonus_armadura = int(input("Qual o bônus da armadura/escudo que está usando? "))
            
            ca_total = 10 + mod_destreza + bonus_armadura
            print(f"👉 Resultado: Sua Classe de Armadura é {ca_total}. O inimigo precisa tirar {ca_total} ou mais para te acertar!")

        # --- OPÇÃO 3: PROCURAR ---
        elif escolha == '3':
            print("\n--- TESTE DE PERCEPÇÃO ---")
            mod_sabedoria = int(input("Qual o seu modificador de Sabedoria? "))
            proficiencia = int(input("Qual o seu bônus de proficiência (digite 0 se não for treinado)? "))
            
            dado = random.randint(1, 20)
            total = dado + mod_sabedoria + proficiencia
            print(f"👉 Resultado: Dado ({dado}) + Sabedoria ({mod_sabedoria}) + Proficiência ({proficiencia}) = TOTAL: {total}")

        # --- OPÇÃO 4: SAIR ---
        elif escolha == '4':
            print("\nEncerrando o programa... Bom jogo e cuidado com os dragões! 🐉")
            break # Isso quebra o 'while' e finaliza o programa
            
        else:
            print("\n⚠️ Opção inválida! Digite 1, 2, 3 ou 4.")

# Isso faz o programa começar
iniciar_rpg()