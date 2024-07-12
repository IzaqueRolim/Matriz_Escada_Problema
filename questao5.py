# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
numLinha = int(input())
numColuna = int(input())

matriz = []
for i in range(numLinha):
    linha = []
    for j in range(numColuna):
        linha.append(int(input()))
    matriz.append(linha)
    
message = 'S'

for i in range(numLinha):
    primeiroElemento = -1
    for j in range(numColuna):
        if matriz[i][j] != 0:
            primeiroElemento = j
            break
    
    if primeiroElemento == -1:
        for k in range(i + 1, numLinha):
            for l in range(numColuna):
                if matriz[k][l] != 0:
                    message = 'N'
                    break
    else:
        for k in range(i + 1, numLinha):
            for l in range(primeiroElemento + 1):
                if matriz[k][l] != 0:
                    message = 'N'
                    break    
        if message == 'N':
            break

print(message)
