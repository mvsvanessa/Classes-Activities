def cabecalho():
    from time import sleep
    print("""\t\t\t
      ====================================
       | SEJA BEM VINDO AO JOGO DA FORCA |
      ====================================
    """)
    print()
    sleep(1.2)


def corpo(valor, chances):
    import os
    from time import sleep

    os.system('cls')
    sleep(0.3)
    if valor == 1:
        print(f""" 
        ℂℍ𝔸ℕℂ𝔼𝕊 {chances}
         ------  
        /     |  
        |    (_) 
        |        
        |        
        |        
       _|____""")

    if valor == 2:
        print(f"""
        ℂℍ𝔸ℕℂ𝔼𝕊 {chances}
         ------  
        /     |  
        |    (_) 
        |     |  
        |        
        |        
       _|____""")

    if valor == 3:
        print(f"""
        ℂℍ𝔸ℕℂ𝔼𝕊 {chances}
         ------  
        /     |  
        |    (_) 
        |     |\  
        |        
        |        
       _|____""")

    if valor == 4:
        print(f"""
        ℂℍ𝔸ℕℂ𝔼𝕊 {chances}
         ------  
        /     |  
        |    (_) 
        |    /|\   
        |        
        |        
       _|____""")

    if valor == 5:
        print(f"""
        ℂℍ𝔸ℕℂ𝔼𝕊 {chances}
         ------  
        /     |  
        |    (_) 
        |    /|\   
        |     |
        |    / 
        |        
       _|____""")


def perdeu(correto):
    from time import sleep
    sleep(0.3)
    print(f"Voce perdeu... A palavra correta é [ {correto} ]")


def ganhou():
    import os
    from time import sleep
    os.system('cls')
    sleep(0.3)
    print("Você ganhou!")

