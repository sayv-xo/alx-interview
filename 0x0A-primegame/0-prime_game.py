#!/usr/bin.python3
"""prime game"""


def isWinner(x, nums):
    if not nums or x < 1:
        return None

    n = max(nums)
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    # Sieve of Eratosthenes
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    primes = [i for i in range(n + 1) if sieve[i]]
    players = {"Maria": 0, "Ben": 0}

    for num in nums:
        even_count = sum(1 for p in primes if p <= num and p % 2 == 0)
        odd_count = sum(1 for p in primes if p <= num and p % 2 == 1)

        if even_count > odd_count:
            players["Maria"] += 1
        else:
            players["Ben"] += 1

    if players["Maria"] == players["Ben"]:
        return None
    return max(players, key=players.get)
