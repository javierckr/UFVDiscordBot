import random


def main():
    with open("recursos/chistes/asciis.txt") as f:
        lines = random.sample(f.readlines(), 1)
        return str(lines[0]).replace("88888", "\n")
        f.close()
