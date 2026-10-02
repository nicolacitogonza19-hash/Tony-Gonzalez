def es_primo(n):
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


for numero in range(1, 51):
    if es_primo(numero):
        print(numero)
