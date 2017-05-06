
numSeeds = input()

seedlings = [int(x) for x in input().split(' ')]

seedlings = sorted(seedlings)[::-1] # plant longest wait to shortest

wait = 0
for t, ti in enumerate(seedlings):
    t += 1 # start counting day 1
    maturity = t + ti + 1 # 1 day to plant seed
    wait = max(wait,maturity)

print(wait)

