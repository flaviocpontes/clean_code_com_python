lista = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            if i + j + k == 25:
                lista.append((i, j, k))
print(lista)

print([(i, j, k)
       for i in range(10)
       for j in range(10)
       for k in range(10)
       if i + j + k == 25])