
palavras_reservadas = {
    "if": "estrutura condicional",
    "else": "condicional alternativa",
    "while": "estrutura de repetição",
    "return": "retorno de função",
    "int": "declaração de variável inteira",
    "float": "declaração de variável real",
    "print": "impressão na tela",
    "for": "estrutura de laço",
    "break": "interrupção de laço",
    "def": "declaração de função",
}


def pesquisar_palavra(palavra):
    if palavra in palavras_reservadas:
        significado = palavras_reservadas[palavra]
        print(f"'{palavra}' é uma palavra reservada: {significado}")
    else:
        print(f"'{palavra}' não é uma palavra reservada.")


entrada = input("Digite uma palavra para verificar se é reservada: ").strip()
pesquisar_palavra(entrada)
