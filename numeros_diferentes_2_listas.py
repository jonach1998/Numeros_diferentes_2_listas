# # A la antigua
a = [1, 10, 5, 3, 8]
b = [8, 80, 100, 3, 10]
c = list()
notrepeted = 0

for item1 in a:
    for item2 in b:
        if item1 != item2:
            notrepeted = 1
        else:
            notrepeted = 0
            break
    if notrepeted:
        c.append(item1)

for item1 in b:
    for item2 in a:
        if item1 != item2:
            notrepeted = 1
        else:
            notrepeted = 0
            break
    if notrepeted:
        c.append(item1)
print(c)

# Forma optimizada
c = [item for item in a + b if item not in b or item not in a]
print(c)
