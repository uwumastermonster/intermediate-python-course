def main():
    import random
    dice_rolls = 2;
    roll = [];
    for i in range(0,dice_rolls):
        roll.append(random.randint(1,20));
    print(f'You rolled {roll}')
    for x in roll:
        if x==1:
            print (f'You rolled a {x}! Critical fail!')

if __name__== "__main__":
  main()
