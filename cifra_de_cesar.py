alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
caracteres_especiais = [' ', '-', ',', '!', '?', '.', '"']

#* Função que faz a criptografia
def cifra_de_cesar(palavra, x, acao):
    pos = [] # *Vetor que indica a posição
    for i in palavra:
        if i in caracteres_especiais:
            pos.append(i)
        for j in alfabeto:
            if i.upper() == j:
                pos.append(alfabeto.index(j))
                continue

    #* Verificando a direção que deve caminhar
    if acao == 'c':
        for i in range(len(pos)):
            if pos[i] in caracteres_especiais:
                continue
            pos[i] += x
            if pos[i] > 25: #* Verificando se passou do 'Z'
                pos[i] = pos[i] % 26
    else:
        for i in range(len(pos)):
            if pos[i] in caracteres_especiais:
                continue
            pos[i] -= x

    #* Montando a nova palavra
    nova_palavra = []
    for i in pos:
        if i in caracteres_especiais:
            nova_palavra.append(i)
        else:
            nova_palavra.append(alfabeto[i])

    nova_palavra = ("".join([str(i) for i in nova_palavra])).capitalize()

    return nova_palavra
