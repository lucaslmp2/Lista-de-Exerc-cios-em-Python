n = 100
ultimo=0
penultimo=1

count=3
while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        if(termo) in range(0,100):
            print(termo)
    