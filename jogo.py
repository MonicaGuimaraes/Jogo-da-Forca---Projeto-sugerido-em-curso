chances = 3
digitadas = []

print("Olá vamos jogar o 'Jogo da Forca'.")
while True:
    tema = input("Digite o tema da palavra que irá escolher, para ajudar quem irá descobrir: ")
    if not tema.isalpha():
        print("Isso não é uma palavra, digite novamente")
        continue
    else:
        print(tema)
        break
while True:
    secreto = input("Digite uma palavra para o jogo da forca: ")
    if not secreto.isalpha():
        print("Isso não é uma palavra, digite novamente")
        continue
    else:
        print(32 * '\n')
        print('Já pegamos a sua palavra. Chame alguém para tentar advinha-lá')
        print("""              ______            
              |    |
              |   ( )    (° °)
              |         --|||--
              |    OOoo__ / \   """)
        print(22 * '\n')
        break
print(f"O tema da palavra é: {tema}")
print(f'A quantidade de caracteres é: {len(secreto)}')

while True:
    if chances <= 0:
        print('Você perdeu! Acabaram suas chances.')
        print("""                 
                            __________     (Socorsqrqrq!)   
                            |      __|__  o
                            |     |(ToT)|°  
                            |      ¨¨¨¨¨
                            |     --|||--
                            |       / \ 
                            |""")
        break
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra! Não vale trapacear.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra "{letra}" está na palavra secreta!')
    else:
        print(f'Que pena! A letra "{letra}" não está na palavra secreta...')
        chances -= 1
        print(f"Você ainda tem {chances} chances.")
        digitadas.pop()

    secreto_temporario = ""
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += "*"

    if secreto_temporario == secreto:
        print(f"Você ganhou! A palavra secreta era: {secreto}.")
        print("""                 
                                  (UFA! Você Me Salvou!)   
                                  o
                           (°u°) °  
                          --|||--
                            / \ """)
        break
    else:
        print(f"Como a palavra está até agora: {secreto_temporario}")
