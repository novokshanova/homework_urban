numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for numb in numbers:
    if numb < 2:
        continue

    is_prime = True
    for i in range(2, numb):
        if numb % i == 0:
            is_prime = False
            break

    if is_prime:
        primes.append(numb)
    else:
        not_primes.append(numb)

print(f"Primes: {primes} Not Primes: {not_primes}")
