from scipy import interpolate
from numpy import poly1d

# the following function opens the requested file
# the parameter 'option' is an integer in [1:3] (closed)
def openFile(option):
    if option == 1: return open("Solido", "r")
    elif option == 2: return open("Laminado", "r")
    else: return open("Misturado", "r")

# that function separates the points for the interpolation
# it receives the lines and the index after the horizintal axis here crossed
def selectPoints(lines, k):
    H, B = [], []
    r = 3 # the inverval will be [k - r: k + r)

    for j in range(k - r, k + r): #[k-4, k+4)
        line = lines[j]
        lineSplited = line.split("\t")

        H.append(float( lineSplited[0] ))
        B.append(float( lineSplited[1][ : len(lineSplited[1]) - 1] ))

    return H, B

# main function
def main():
    print("Entre com uma das seguintes opções: ")
    print("\t * 1 - Solido")
    print("\t * 2 - Laminado")
    print("\t * 3 - Misturado")

    option = int(input("\t > "))

    if option in [1, 2, 3]: file = openFile(option)
    else:
        print("Resultado de entrada deve ser 1, 2 ou 3. Reinicie o programa...")
        return

    lines = file.readlines()
    """
    - Linhas 0, 1 e 2 devem ser descartadas; são apenas comentários.
    - Linhas com os dados têm a forma: "%f\t%f\n".
    As linhas de código a seguir leem os floats na forma acima, linha a linha,
    para determinar o cruzamento do gráfico no eixo vertical. Isso é feito
    para determinar um array a ser utilizado na interpolação que se segue.
    """

    """
    As duas linha a seguir são feitas (e explicadas) em partes no loop abaixo
    e servem apenas como uma forma de inicializar as variáveis B_current e
    B_before. A inicialização começa pela linha 3 do código
    """
    B_current = float(lines[3].split("\t")[1][ : len(lines[3].split("\t")[1]) - 1])
    B_before = B_current

    for k in range(4, len(lines)): # loop começa da linha 4
        line = lines[k] # each line have the form H\tB\n
        lineSplited = line.split("\t") # now, this have the form [H(%f), B(%f)\n]

        B_before = B_current # save the preceding to compare
        B_current = float( lineSplited[1][ : len(lineSplited[1]) - 1] )

        if (B_before > 0 and B_current < 0): # crossed the coercive field...
            """
            The current index is 'k'. To interpolate we will take 4 points
            after and 4 points before the zero; so, from k - 4 (closed) to
            k + 4 (open)
            """
            xAxis, yAxis = selectPoints(lines, k)
            print(xAxis)
            print(yAxis)
            poly = interpolate.lagrange(xAxis, yAxis)
            break
        # end if
    #end for

    H_coercive = poly(0)
    print("Coercive field: %.3f" % H_coercive)

    file.close()
#end main

main()
