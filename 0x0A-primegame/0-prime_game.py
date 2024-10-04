#!/usr/bin/python3
"""prime game"""


def isWinner(x, nums):
    """returns the name of the player that won the most rounds"""
    if x <= 0 or nums is None or len(nums) == 0:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
        else:
            if play_game(n):
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None


def play_game(n):
    """simulates one round of the game"""
    primes = [False, False] + [True] * (n - 1)
    current_player = 0

    for i in range(2, n + 1):
        if primes[i]:
            for j in range(i * 2, n + 1, i):
                primes[j] = False
            current_player = 1 - current_player

    return current_player == 1
