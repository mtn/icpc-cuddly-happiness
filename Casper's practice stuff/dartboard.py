import math

meanPie = 10.5 # (1+...+20)/20

def probin(R,sigma, dr=.001):
    return 1 - math.e**( - R**2 / 2 / sigma**2)

#def probin(R,sigma,dr=.001):

#   r = 0
#    area = 0
#    while r < R:
#        area += r * math.e**(-r**2 / 2 /sigma *2




inBull, bullA, i3r, o3r, i2r, o2r = [float(x) for x in input().split(' ')]
sigma = float(input())




def prob_btw(r,R,sigma):
    return probin(R,sigma) - probin(r,sigma)

expected = 50 * probin(inBull,sigma) \
           + 25 *          prob_btw(inBull,bullA, sigma)   \
           + meanPie *     prob_btw(bullA , o2r , sigma) \
           + 2 * meanPie * prob_btw(i3r   , o3r , sigma) \
           + meanPie *     prob_btw(i2r   , o2r , sigma)

print(expected)
