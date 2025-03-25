import random

def sortear_palavra():
    palavras = [
        "abacaxi", "acordar", "alegria", "banco", "bola", "carro", "cavalo", "chave", "colina", "coração",
        "caminho", "dente", "escola", "estrela", "futuro", "gato", "guitarra", "livro", "macaco", "mundo",
        "mestre", "nuvem", "olho", "parque", "pessoa", "piano", "quadro", "rosa", "segredo", "sol",
        "tigre", "trompete", "vila", "vitoria", "volta", "zebra", "zoo", "amigo", "paz", "panela",
        "plano", "galo", "jogo", "pico", "teto", "mato", "fogo", "vento", "pato", "gelo",
        "cachorro", "oculos", "salada", "banana", "paradeiro", "mestre", "esmalte", "luz", "caminhar", "ponte",
        "mala", "panela", "batata", "arroz", "caneta", "coelho", "tartaruga", "mesa", "peca", "trava",
        "caverna", "pingente", "chaveiro", "janela", "cabelo", "bicicleta", "luz", "caixa", "aviao",
        "navio", "violao", "pescador", "castelo", "raiz", "deserto", "famoso", "escuro", "divertido",
        "paraiso", "cozinha", "geladeira", "fazer", "camisa", "agenda", "moeda", "dente", "biscoito", 
        "grande", "espaco", "vermelho", "bordo", "jardim", "bola", "raquete", "caderno", "chocolate", "bolacha"
    ]
    return random.choice(palavras)

def exibir_lacunas(palavra, letras_descobertas):
    exibir = ""
    for letra in palavra:
        if letra in "aeiou" or letra in letras_descobertas:
            exibir += letra + " "
        else:
            exibir += "_ "
    print(exibir)

def jogar():
    palavra = sortear_palavra()
    letras_descobertas = []
    tentativas = 6

    print("Bem-vindo ao jogo da forca!")

    while tentativas > 0:
        exibir_lacunas(palavra, letras_descobertas)
        tentativa = input("Digite uma letra: ").lower()

        if not tentativa.isalpha() or len(tentativa) != 1:
            print("Por favor, digite uma letra válida!")
            continue

        if tentativa in palavra:
            letras_descobertas.append(tentativa)
        else:
            tentativas -= 1
            print("letra errada, ocê tem", tentativas, "tentativas restantes.")

        acertou = True
        for letra in palavra:
            if letra not in letras_descobertas and letra not in "aeiou":
                acertou = False

        if acertou:
            print(f"parabéns! Você acertou a palavra: {palavra}")
            return

    print(f"fim de jogo, a palavra era: {palavra}")

jogar()