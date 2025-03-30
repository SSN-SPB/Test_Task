def square(n, cache={}):
    print(f"cache init: {cache}")
    if n in cache:
        print("taken from cache:")
        return cache[n]
    else:
        print("Calculating result:")
        result = n * n
        cache[n] = result
        print(f"cache: {cache}")
        return result


print(square(4))
print(square(4))
print(square(5))
print(square(5))
print(square(5, cache={}))
