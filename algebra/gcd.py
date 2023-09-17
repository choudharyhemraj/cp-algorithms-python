def gcd(a,b):
    a,b = max(a,b),min(a,b)
    while b:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    print(gcd(6,15), 3)
    print(gcd(117,13),13)