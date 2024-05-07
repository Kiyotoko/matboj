from tqdm import tqdm

def quer_sum(n: int) -> int:
    """Gibt die Quersumme einer Zahl zurück."""
    q = 0
    j = n
    while (j > 0):
        t = j % 10
        q += t
        j //= 10
    return q


def evaluated(n: int) -> float:
    """Gibt den Performance Score n/q(n) zurück."""
    return n / quer_sum(n)


def main():
    """
    Sei q(n) die Quersumme einer natürlichen Zahl n. Finde die dreistellige
    natürliche Zahl m, für die der Quotient m/q(m) minimal ist.
    """
    minimum = 10 ** 3
    score = evaluated(minimum)
    for i in tqdm(range(10 ** 2, 10 ** 3)):
        if (score > evaluated(i)):
            score = evaluated(i)
            minimum = i
    print(minimum, score)


if __name__ == "__main__":
    main()