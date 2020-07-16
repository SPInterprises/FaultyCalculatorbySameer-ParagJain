def main():
    print("Welcome to my smarty caclulator  \n",end=" This Code is developed by Sameer\Parag Jain:\n")
    char1=int(input("Enter your First Number\n"))
    operator=input("Choose your operator which yu want to calculate:\n Press + for Addition \n Press - For Subtraction \n Press * for Multiplication \n Press / for Divide \n Press ** For Power \n Press % for Percentage\n")
    char2=int(input("Enter your Second Number\n"))
    if char1==45 and char2==9 and operator=="+":
        print("Your answer is 77")
    elif char1==45 and char2==8 and operator=="-":
        print("Your answer is 32")
    elif char1==8 and char2==9 and operator=="*":
        print("Your answer is 65")
    elif char1==48 and char2==12 and operator=="/":
        print("Your answer is 8")
    elif operator=="+":
        print("Your answer is ", char1+char2)
    elif operator=="-":
        print("Your answer is ",char1-char2)
    elif operator=="*":
        print("Your answer is ", char1*char2)
    elif operator=="/":
        print("Your answer is ", char1/char2)
    elif operator=="**":
        print("Your answer is ",char1**char2)
    elif operator=="%":
        print("Your answer is ",char1*char2/100)
    else:
        print("you press invalid key")
    print("Do you want to Calculate again ? y for yes and n for not \n")
    user_choice=""
    while (user_choice!="y" and user_choice!="n"):
        user_choice=input()
        if user_choice=="y":
            main()
        if user_choice=="n":

            print("Thank you for using Smarty calculator\n Have a great day")
            exit()

main()