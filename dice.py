import random
import sys

def roll(sides=6):
    return random.randint(1, sides)

if __name__ == "__main__":
    sides = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    print(f"You rolled a {roll(sides)} (d{sides})")
