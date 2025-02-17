import random

# p - 1 = 2**k * q    (q: odd number)
# a**q != 1 (mod p) or {a**q != p-1 (mod p) and a**(2q) != p-1 (mod p) and ... and a**(2(k-1)q) != p-1 (mod p)} 
# => p is composite number
def is_prime(p: int, round: int = 10) -> bool:
    if p == 2: 
        return True
    if p < 2 or (p & 1) == 0:
        return False
    
    k, q = 0, p - 1
    while (q & 1) == 0:
        k += 1
        q >>= 1

    for _ in range(round):
        a = random.randint(2, p-1)
        x = pow(a, q, p)
        if x == 1 or x == p - 1:
            continue
        is_composite = True
        for _ in range(k):
            x = pow(x, 2, p)
            if x == p - 1:
                is_composite = False
                break
        if is_composite:
            return False
    return True


def main():
    print(is_prime(101))

if __name__ == "__main__":
    main()
