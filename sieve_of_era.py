def sieve_of_era(n):
    multiples = []
    for i in range(2, n+1):
        if i not in multiples:
            print (i)
            for j in range(i*i, n+1, i):
                multiples.append(j)

n = int(input("Enter the number for calculating primes below your number :\n"))
sieve_of_era(n)