import random

# Você pode colocar isso como a Opção 5 no seu menu principal
def rolar_dano_generico():
    print("\n--- 🩸 CALCULADORA DE DANO GENÉRICA ---")
    
    # 1. Pegando as informações da arma/magia principal
    qnt_dados = int(input("Quantos dados a arma/magia usa? (Ex: 1, 2, 8): "))
    faces = int(input("Qual é o tipo do dado? (Ex: 4, 6, 8, 10, 12, 20): "))
    modificador = int(input("Qual o modificador de atributo? (Digite 0 para magias): "))
    
    # 2. Perguntando sobre danos extras (veneno, fogo, furtivo, etc)
    tem_extra = input("Tem dano extra de magia ou habilidade? (s/n): ").strip().lower()
    
    dano_extra_total = 0
    rolagens_extras = []
    
    if tem_extra == 's':
        qnt_extra = int(input("Quantos dados extras? "))
        faces_extra = int(input("De quantas faces é o dado extra? "))
        
        for _ in range(qnt_extra):
            dado_extra = random.randint(1, faces_extra)
            rolagens_extras.append(dado_extra)
            dano_extra_total += dado_extra
            
    # 3. Rolando o dano base
    soma_base = 0
    rolagens_base = []
    
    for _ in range(qnt_dados):
        dado = random.randint(1, faces)
        rolagens_base.append(dado)
        soma_base += dado
        
    # 4. Calculando tudo
    dano_final = soma_base + modificador + dano_extra_total
    
    # 5. Mostrando o resultado bonito para o Mestre
    print("\n" + "="*30)
    print("🎯 RESULTADO DO DANO")
    print("="*30)
    print(f"Rolagem Base ({qnt_dados}d{faces}): {rolagens_base} = {soma_base}")
    print(f"Modificador: +{modificador}")
    
    if tem_extra == 's':
        print(f"Dano Extra ({qnt_extra}d{faces_extra}): {rolagens_extras} = {dano_extra_total}")
        
    print("-" * 30)
    print(f"🩸 DANO TOTAL APLICADO: {dano_final}!")
    print("="*30)

# Para testar a função isolada:
# rolar_dano_generico()
