
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

def main():
    a, b = -3, -10
    x, y, gcd = ex_euc(a, b)
    print(f"{a}*{x} + {b}*{y} = {gcd}")

if __name__ == "__main__":
    main()

