def binary_exponentiation(base: float, exp: int) -> float:
    power = base
    result = 1
    mode = 10 ** 9 + 7
    while exp:
        if 1 & exp:
            result *= power % mode 
        power *= power % mode 
        exp = exp >> 1
        print(exp)
    
    return result 


if __name__ == '__main__':
    print(binary_exponentiation(3,13), 1594323)
    print(binary_exponentiation(4,806166225460393), 1024)