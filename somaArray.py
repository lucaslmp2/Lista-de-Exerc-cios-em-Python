numeros = []
somaArray = 0
count = 0
while(count<=2):
    numero = float(input("Digite um número para somar: "))
    numeros.append(numero)
    somaArray += numero
    print("Array:",numeros," - soma de números do array:",somaArray)
    count+=1
    