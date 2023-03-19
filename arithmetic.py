import random
operations = ["+", "-", "*"]
count = 0
mark = 0
yes = ["yes", "Yes", "YES", "y"]
while count < 5:
    level = int(input("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
"""))
    if level == 1:
        while count < 5:
            a = f"{random.randint(2, 9)} {random.choice(operations)} {random.randint(2, 9)}"
            print(a)
            while True:
                try:
                    b = int(input())
                    break
                except ValueError:
                    print("Wrong format! Try again.")
                    continue
            if eval(a) == b:
                print("Right!")
                count += 1
                mark += 1
            else:
                print("Wrong!")
                count += 1
                mark += 0
        e = input(f"Your mark is {mark}/5. Would you like to save the result? Enter yes or no.")
        if e in yes:
            name = input("What is your name?")
            g = open("results.txt", "a")
            g.write(f"{name}: {mark}/5 in level 1 (simple operations with numbers 2-9).")
            print("The results are saved in 'results.txt'.")
    if level == 2:
        while count < 5:
            c = int(random.randint(11, 29))
            print(c)
            while True:
                try:
                    b = int(input())
                    break
                except ValueError:
                    print("Wrong format! Try again.")
                    continue
            if b == c * c:
                print("Right!")
                count += 1
                mark += 1
            else:
                print("Wrong!")
                count += 1
                mark += 0
        f = input(f"Your mark is {mark}/5. Would you like to save the result? Enter yes or no.")
        if f in yes:
            g = open("results.txt", "a")
            name = input("What is your name?")
            g.write(f"{name}: {mark}/5 in level 2 (integral squares of 11-29).")
            print("The results are saved in 'results.txt'.")
    else:
        print("Incorrect format.")
        continue
