def remove(source, size, idx):
    
    if idx < 0 or idx >= size:
        return
    
    for i in range(idx, size - 1):
        source[i] = source[i + 1]
    
    source[size - 1] = 0

source = [10, 20, 30, 40, 50, 0, 0]
remove(source, 5, 2)
print(source)