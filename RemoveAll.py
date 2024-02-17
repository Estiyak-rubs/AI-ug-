def removeAll(source, size, element):
    
    i = 0
    while i < size:
        if source[i] == element:

            for j in range(i, size - 1):
                source[j] = source[j + 1]
            size -= 1 
        else:
            i += 1
    
    for i in range(size, len(source)):
        source[i] = 0

source = [10, 2, 30, 2, 50, 2, 2, 0, 0]
removeAll(source, 7, 2)
print(source)