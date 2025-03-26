def calcula_fatorial(numero:int) -> int:
    "Utilizando 'for', crie um loop para calcular o fatorial de um número"

def batalha_naval():
    """Gere uma lista com 10 números aleatórios de 0 a 100. Pergunte um número ao usuário. Se o número NÃO estiver ma lista, o usuário 
    ganha um ponto. Caso esteja, deve aparecer uma mensagem de derrota, a quantidade de pontos e o laço é interrompido.  """

def adivinhe_o_numero():
    """Crie um jogo de adivinhação onde o computador escolhe um número aleatório entre 1 e 20, em que o usuário tem que adivinhar qual é
    esse número. O programa deve dar dicas, dizendo se o número adivinhado é maior ou menor que o número correto. O jogo deve continuar
    até o usuário adivinhar corretamente."""

def tabuada_do_1_ao_9():
    "Utilizando um laço de iteração (ciclo de repetição), imprima na tela a tabuada do 2 ao  9. Pode-se usar 'for' ou 'while'"

def formando_palavras():
    """Sorteie uma palavra da lista 'palavras', imprima na tela e solicite ao usuário que forme outras palavras utilizando as letras
    contidas palavra exibiida. 
    Exemplo:
        MELANCIA
            - macia
            - mel
            ...
    Deverá haver um laço, onde a cada iteração será capturada a resposta do usuário validada. O laço é interrompido quando o usuário 
    digitar uma palavra incorreta. Deverá imprimir na tela a quantidade de palavras acertadas,
    """
    palavras = ['MELANCIA', 'CONSTITUCIONALISTA', 'BRASILEIRA']
    
    palavra_sorteada = 'Sorteie aqui a palavra'
    print(palavra_sorteada)

    palavra_usuario = input("Forme uma palavra à partir de {palavra_sorteada}") # corrija o erro de síntaxe desta linha

    # for ??????? in ?????????:
        # verifique 
        # retorne se a palavra não for válida



fat = calcula_fatorial(5)
print(fat)
batalha_naval()
adivinhe_o_numero()
tabuada_do_1_ao_9()
formando_palavras()