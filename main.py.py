import random

print("Welcome to Shashank Kingdom 👑")
while True:
    print("Select Game 👇")
    print("Press 1 for 'Head or Tail'")
    print("Press 2 for 'Rock, Paper, Scissor'")
    print("press 3 for 'EXIT'")
    user = input("Enter 1,2,3 : ")

    if user == "1":
        print("Welcome to the Game of Heads and Tails"),
        print("Please Select your option 👇")
    
        while True:
            Toss = ["Heads", "Tails"]
            computer = random.choice(Toss)

            user_choice = input("Enter Heads or Tails : ").capitalize()
            print("Computer : ", computer)
    
            if user_choice == computer:
                print("Congratulation You Won! 🎉")
            else:
                print("Opps! You Loss 😣")

            again = input("Play again? (yes/no): ").lower()
            if again != "yes":
                break
    
    elif user == "2":
        print("Welcome to 'Rock, Paper, Scissor' Game")
    
        while True:
            Choices = ["Rock","Paper", "Scissors"]

            computer = random.choice(Choices)
            user = input("Enter Rock, Paper, Scissors : ")

            print ("Computer : ", computer)
            if user == computer:
                print("DRAW")
            elif user == "Rock" and computer == "Scissors":
                print("YOU WIN")
            elif user == "Paper" and computer == "Rock":
                print("YOU WIN")
            elif user == "Scissors" and computer == "Paper":
                print("YOU WIN")
            else:
                print("Computer Wins")
            again = input("Play again? (yes/no): ").lower()
            if again != "yes":
                break

    elif user == "3":
        confirm = input("Are you sure you want to exit? (yes/no): ").lower()

        if confirm == "yes":
            print("Thanks for playing with Shashank 👑")
            break
        else:
            print("Returning to menu...")

    else:
        print("Invalid Selection")
