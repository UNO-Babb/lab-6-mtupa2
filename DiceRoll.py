#DiceRoll.py
#Name:
#Date:
#Assignment:
import random

def main():
    # Create a list to hold counts for sums from 2 to 12
    rolls = [0] * 11 

    # Roll two dice 100 times
    for r in range(100):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        rolls[total - 2] += 1

    # Print statistics for each possible sum
    sum_value = 2
    for count in rolls:
        print(sum_value, ":", count)
        sum_value += 1

if __name__ == '__main__':
    main()
