
def mediana(array):
    if len(array) % 2 == 0:
        return ((array[len(array)//2 - 1]) + (array[len(array)//2])) / 2
    else:
        return array[len(array)//2]

def media(array):
    return sum(array) / len(array)

def range(array):
    return array[len(array)-1] - array[0]

def q1(array):
    mid = len(array)//2
    lArray = array[:mid]
    primeiroQuartil = mediana(lArray)
    return primeiroQuartil

def q3(array):
    mid = len(array)//2
    if len(array) % 2 == 0:
        rArray = array[mid:]
    else:
        rArray = array[mid+1:]
    terceiroQuartil = mediana(rArray)
    return terceiroQuartil

def rangeQ(array):
    return q3(array) - q1(array)

def variancia(array):
    mediaArray = media(array)
    soma = 0
    for i in array:
        soma += (i - mediaArray) ** 2
    return soma / (len(array) - 1)

def desvioPadrao(array):
    var = variancia(array)
    return var ** 0.5
    
array = [15, 4, 3, 8, 15, 22, 7, 9, 2, 3, 3, 12, 6]
arrayOrdenado = sorted(array)

print(arrayOrdenado)

print("Mediana = {}".format(mediana(arrayOrdenado)))
print("Media = {:.2f}".format(media(arrayOrdenado)))
print("Amplitude = {}".format(range(arrayOrdenado)))
print("Primeiro Quartil = {}".format(q1(arrayOrdenado)))
print("Terceiro Quartil = {}".format(q3(arrayOrdenado)))
print("Amplitude interquartil = {}".format(rangeQ(arrayOrdenado)))
print("Variancia = {:.2f}".format(variancia(arrayOrdenado)))
print("Desvio padrao = {:.2f}".format(desvioPadrao(arrayOrdenado)))




