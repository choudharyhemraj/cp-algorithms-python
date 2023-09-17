tests = int(input())

def modules(x,y,m):
    result = 1
    power = x 
    while y:
        if 1 & y:
            result *= power 
            result %= m 
        power *= power 
        power %= m
        y >>= 1
    print(result)

for test in range(tests):
    inp = input()
    inp = inp.split()
    inp = list(map(int,inp))
    x,y,n = inp
    modules(x,y,n)

