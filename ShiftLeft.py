def shiftLeft(source, k):
    length = len(source)
    for i in range(length):
        if i + k < length:
            source[i] = source[i + k]
        else:
            source[i] = 0
    print(source)

source = [10, 20, 30, 40, 50, 60]
shiftLeft(source, 3)