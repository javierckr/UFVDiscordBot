import random


def main():
    with open("recursos/chistes/chistescortos.txt") as f:
        lines = random.sample(f.readlines(), 1)
        # print(lines)
        return str(lines).strip("[]'-")[: len(lines) - 3]
        f.close()
