import math

def g(x):
    return (x - (1.3 * (x * math.log(x, 10) - 1)))

P0 = 1
for i in range (20):
    P1 = g(P0)
    print(1+i, P1)
    P0 = P1

print(g(2.5061841456175986))