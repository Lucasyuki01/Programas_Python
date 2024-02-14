#Exercicio: Questionario, onde o usuario tem que responder as perguntas e se acertar acumula pontos

perguntas = [ #Dictonary com algumas perguntas
    {
        'Pergunta':'Quanto é 2+2?',
        'Opções':['1','3','4','5'],
        'Resposta':'4'
    },

    {
        'Pergunta':'Quanto é 5*5?',
        'Opções':['25','55','10','51'],
        'Resposta':'25'
    },

    {
        'Pergunta':'Quanto é 10/2?',
        'Opções':['4','5','2','1'],
        'Resposta':'5'
    },
]

cont = 0 #Iniciando a pontuacao em zero

for pergunta in perguntas: #laço de repeticao para passar de perguta em pergunta
    print('Pergunta:',pergunta['Pergunta'])#print da questao
    
    opcoes = pergunta['Opções']#colocando as Opcoes em uma variavel para facilitar o manuseio

    for i, opcao in enumerate(opcoes):#Laço de repetição para listar e enumerar as opções
        print(f'{i})', opcao) #Print da opção com seu indice
    print()

    resposta = input('Escolha uma opção: ')#input da resposta do usuario

    acertou = False #criação da variavel como false
    resposta_int = None #criação da variavel para resposta em numero inteiro
    qtd_opcoes = len(opcoes) #variavel para guardar o umero de opçoes
    
    if resposta.isdigit(): #Verificação se o valor dado é um digito
        resposta_int = int(resposta) #se for é armazenada na variável

    if resposta_int is not None: #segunda verificação se algo foi digitado
        if resposta_int >= 0 and resposta_int < qtd_opcoes: #verificando se a resposta dada esta dentro da range
            if opcoes[resposta_int] == pergunta['Resposta']: #Verifica se a resposta dada bate com a resposta correta
                acertou = True #torna a variavel acertou True
                cont = cont +1 #adiciona um ponto na contagem

    if acertou: #condicioal caso tenha acertado
        print('Acertou\n')
    else: #condicioal caso tenha errado
        print('Errou\n')
    
print(f'Você acertou {cont} de 3 perguntas!') #fora do laço, mostra o numero de acertos do usuario
