import random
# random is imported so that computer could select randomly
def rules():
    print("                             !!!!WELCOME!!!!         ")
    print("                          NUMBER GUESSING GAME \n\n")
    print("I WILL THINK OF A NUMBER BETWEEN 1 TO 100 ")
    print("YOU HAVE TO GUESS THE NUMBER ")
    print("YOU WILL KNOW IF YOUR GUESS IS TOO LOW OR TOO HIGH")
    # def rules() is to show all the instruction require to play the game 

def game():
    number= random.randint(1,100)
    a=0 #a is number of attempts
    while True:
        guess= int(input("enter your guess: "))
        a=a+1
        #this will make computer chose the random integer and track number of attempts
        if guess > number:
            print("too high, try again")
        elif guess < number:
            print("too low, try again")
        else:
            print("yayy! you won !!")
            print("the number was",number)
            print("you took",a,"attempts")
            break
        #if else statement used to determine wheather the number is too low or too high
        #def main() is the main function
def main():
    rules()
    while True:
        game()
        again=input("do you want to play again?(yes/no)")
        if again=="no":
            print("GOODBYE!!")
            # this will allow user to play the game continuously without running it again and again
            break
main()
