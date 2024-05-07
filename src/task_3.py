from tqdm import tqdm


PRIMES = []
"""Liste aller Primzahlen"""


def is_prime(i: int) -> bool:
    """Gibt zurück, ob eine Zahl i eine Primzahl ist."""
    for j in PRIMES:
        if i % j == 0:
            return False
    return True


for i in tqdm(range(2, 10 ** 3)):
    if is_prime(i):
        PRIMES.append(i)
print(PRIMES)


def matches_condition(n: int) -> bool:
    """Überprüft, ob eine Zahl dem Beweis von De Bouvelle widerspricht."""
    return (6 * n - 1) not in PRIMES and (6 * n + 1) not in PRIMES


def main():
    """
    Der französische Mathematiker De Bouvelle bewies im Jahre 1509 fälschlicherweise, dass
    für alle n ∈ N eine der Zahlen 6n - 1 oder 6n + 1 eine Primzahl sei.
    a) Gib ein Beispiel an, das zeigt, dass er sich geirrt hat.
    b) Zeige, dass es unendlich viele n ∈ N gibt, die diese Aussage widerlegen.
    """

    matched = []
    for i in tqdm(range(2, 10 ** 2)):
        if matches_condition(i):
            matched.append(i)
    print(matched)
    print("Keine Primzahl:", 6 * matched[0], "± 1")


if __name__ == "__main__":
    main()