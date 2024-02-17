def rotateLeft(source, k):

    if not source or k <= 0:
        return
    
    k = k % len(source)
    
    rotated_array = source[k:] + source[:k]
    
    source[:] = rotated_array

source = [10, 20, 30, 40, 50, 60]
rotateLeft(source, 3)
print(source)