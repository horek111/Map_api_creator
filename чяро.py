import random


def generate_password(m):
    digits = "23456789"
    letters = "abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"
    return "".join(random.choices(digits + letters, k=m))


def main(m, n):
    res = [generate_password(m)]
    for i in range(n - 1):
        pas = generate_password(m)
        while pas in res:
            pas = generate_password(m)
        res.append(pas)
    return [generate_password(m) for _ in range(n)]


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
