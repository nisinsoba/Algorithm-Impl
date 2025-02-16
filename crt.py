
def ex_euc(a: int, b: int) -> tuple[int, int, int]:
    x, xx, y, yy = 0, 1, 1, 0
    if b == 0: 
        x, y, b = 1, 0, a
    else:
        while a % b:
            q, r = a // b, a % b
            tmpx, tmpy = xx - q*x, yy - q*y
            xx, yy = x, y
            x, y = tmpx, tmpy
            a, b = b, r
    if b < 0: 
        return -x, -y, -b
    return x, y, b

def inv_mod(a: int, m: int) -> int:
    x, _, gcd = ex_euc(a, m)
    if gcd != 1: 
        raise Exception("gcd(a, m) != 1")
    return x % m

# x = c0 + c1*m1 + c2*m1*m2 + c3*m1*m2*m3 + ... + cn*m1*m2*m3*...*mn  (mod m1*m2*...*mn)
def crt(m: list[int], a: list[int]) -> int:
    c, x, mp = 0, 0, 1
    for m, a in zip(m, a):
        c = (a - x) * inv_mod(mp, m) % m
        x = x + c*mp
        mp *= m
    return x % mp

def main():
    x = crt([3, 5, 7], [2, 3, 2])
    print(f"x = {x}")


if __name__ == "__main__":
    main()