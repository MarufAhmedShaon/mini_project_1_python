#games project
# guessing
# even odd checker
# multiple table 

print("---Welcome to our small nintendo---")

while True:
    print("\nChoose A game:")
    print("1. guess the number")
    print("2. even odd checker")
    print("3. multiple table")
    print("4. exit")

    choice = int(input("Enter your choice (1-4): "))

#---------Game 1----------

    if choice == 1:
     secret  = 7
     guess = 0

     print("Welcome to guess the number(Please guess between (1-10))")

     while guess != secret:
         guess = int(input("Enter your guess:"))

         if guess < secret:
             print("Too low! Try again.")
         elif guess > secret:
             print("Too high! Try again.")
         else:
             print("You won! Congratulations!")

#---------Game 2----------

    elif choice == 2:
        start = int(input(" Enter first number for even odd checker:"))
        end = int(input("Enter the end number:"))

        print("Even Odd checker.....")

        for num in range(start, end + 1):
            if num % 2 == 0:
                print(num, " is even.")
            else:
                print(num, " is odd.")

#---------Game 3----------

    elif choice == 3:
        number = int(input("Enter a number for multiple table: "))

        print(f"\nMultiplication table for {number}:")

        for i in range(1, 11):
            result = number * i
            print(f"{number} x {i} = {result}")

#---------Exit----------
    elif choice == 4:
        print("For playing games choose 1-3. To exit choose 4.")
        break

    else:
        print("Invalid choice. Please choose a number between 1 to 4.")
