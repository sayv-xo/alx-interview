#!/usr/bin/python3
"""making change"""


def makeChange(coins, total):
    """makeChange function"""
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        num_coins += total // coin
        total = total % coin
    if total != 0:
        return -1
    return num_coins
