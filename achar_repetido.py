"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""

lista_de_listas_de_inteiros = [ #Lista de listas a serem testadas
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  #0
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],   #1 9
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],   #2 2
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],   #3 8
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],  #4 8
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],   #5 2
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],#6 2
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],   #7 1
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],  #8 1
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],   #9 2
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],   #10 5
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],  #11
]

def funcao(listona): #Função que fara o processo
    s1 = set() #criando set s1 que armazenara os itens da lista até encontrar um repetido
    n = 0 #Indice da lista para melhor visualização

    for lista in listona: #Laço de repetição para passar pelas listas da listona
        print(f'Lista {n}') #print para tornar visivel de qual lista a o item é repetido
        n +=1 #Incremento do indice da lista
        pular = False #iniciando como false a variavel que fara o codigo pular

        for item in lista: #laço de repetição para ir de item em item dentro da lista
            if item in s1: #Caso o item esteja dentro de s1, quer dizer que é repetido
                print(item) #Dai printo qual é o item
                pular = True #Torno a variavel true
                break #E dou um break para sair desse for
            
            else: #caso contrário só adiciono o item à s1 para que possa comparar os novos itens
                s1.add(item)
            
        if pular: #uma vez fora do laço pelo break, e com pular = true, limpo s1 para a próxima lista e dou continue para ir para próxima lista
            s1.clear()
            continue
        else:
            print('-1')

        s1.clear() #Mesmo que a condição pular nao seja atingida, devemos limpar s1 para a lista seguinte.

funcao(lista_de_listas_de_inteiros) #chamando a função