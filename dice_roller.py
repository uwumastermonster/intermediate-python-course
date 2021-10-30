def main():
    import random
    dice_rolls = 3;
    roll = [];
    print(roll)
    for i in range(0,dice_rolls):
        roll.append(random.randint(1,6));
    print(f'You rolled {roll}')

if __name__== "__main__":
  main()
