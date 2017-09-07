# pylint: skip-file
# https://www.hackerrank.com/challenges/ctci-coin-change?h_r=next-challenge&h_v=zen
import sys

# Recursion method, too slow for hackerrank
def DP(coin_index, summ, coins, memoize):
  # Base cases
  if summ == 0:
    return 1
  if coin_index == len(coins) or summ < 0:
    return 0
  # Check for memoization
  if memoize[coin_index][summ-1]:
    return memoize[coin_index][summ-1]

  max_coins = summ // coins[coin_index]
  count = 0 
  for n in range(0, max_coins+1):
      remaining_sum = summ - n * coins[coin_index]
      child_count = DP(coin_index+1, remaining_sum, coins, memoize)
      count += child_count
  return count

def DP_it(coins, n, m):
  # 
  memo = [0 for x in range(n+1)]
  memo[0] = 1
  for coin in coins:
    for coin_index in range(coin, n+1):
      memo[coin_index] += memo[coin_index - coin]
  return memo[-1]
      


def make_change(coins, n):
  m = len(coins)
  #memoize[coins][sum]
  memoize = [[None for x in range(n)] for y in range(m)]
  return DP_it(coins, n, m)

f = open('/Users/hakonhukkelas/hacker_rank/cracking_the_coding_interview/DPCoinChange/input.txt','r')
n, m = f.readline().strip().split(' ')

n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in f.readline().strip().split(' ')]
print(make_change(coins, n))


