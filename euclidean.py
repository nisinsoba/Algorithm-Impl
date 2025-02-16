
def euclid(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    if a < 0: 
        return -a
    return a

def main():
    gcd = euclid(-10,-5)
    print(gcd)

if __name__ == "__main__":
    main()

