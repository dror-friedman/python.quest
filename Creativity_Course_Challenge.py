quiz = {
        1: {
            "question": "\nQuestion number 1:\nIn Python, strings are immutable? (true/false)?",
            "answer": "true"
        },
        2: {
            "question": "\nQuestion number 2:\nHow many iterations in total there will be in this loop:\n for i in range(0, 100):\n\tfor j in range(5, 29):\n\t\tdo something",
             "answer": "123"
        },
        3: {
            "question": "\nQuestion number 3:\nWhos the best professor in Ono?",
            "answer": "gnizi"
         }
     }


def game():
    print("\nIn this game there will be 3 questions for you to answer, you have 2 attempts for each question. "
          "\nFor each correct answer you will get 1 point. you need 3 points in total to beat the game."
          "\nGood Luck!")
    score = 0

    for question in quiz:
        attempts = 2
        while attempts > 0:
            print(quiz[question]['question'])
            answer = input("Enter Answer: ")
            check = check_ans(question, answer, attempts, score)
            if check:
                score += 1
                break
            attempts -= 1

    if score == 3:
        print("\nCongratulations! you won the game and can continue to the next task.")
    else:
        print("\nYou didn't gather enough points, the game is over.")
        print("\nPress 1 to try again, or anything else to exit.")
        again = input()
        if again == '1':
            game()
        else:
            print("See ya!")
            exit()

def check_ans(question, ans, attempts, score):
    if quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True
    else:
        attempts -= 1
        if attempts == 0:
            print("No attempts left for this question.")
            return False
        print(f"Wrong Answer :( \nYou have {attempts} attempts left! \nTry again...")
        return False

def exit_func():
    print("Bye! Thanks for your participation.")
    exit()


def main():
    print("""██████╗ ██████╗  ██████╗ ██╗   ██╗███████╗    ██╗   ██╗ ██████╗ ██╗   ██╗     ██████╗ █████╗ ███╗   ██╗    ██████╗ ███████╗ █████╗ ████████╗
    ██╔══██╗██╔══██╗██╔═══██╗██║   ██║██╔════╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔════╝██╔══██╗████╗  ██║    ██╔══██╗██╔════╝██╔══██╗╚══██╔══╝
    ██████╔╝██████╔╝██║   ██║██║   ██║█████╗       ╚████╔╝ ██║   ██║██║   ██║    ██║     ███████║██╔██╗ ██║    ██████╔╝█████╗  ███████║   ██║   
    ██╔═══╝ ██╔══██╗██║   ██║╚██╗ ██╔╝██╔══╝        ╚██╔╝  ██║   ██║██║   ██║    ██║     ██╔══██║██║╚██╗██║    ██╔══██╗██╔══╝  ██╔══██║   ██║   
    ██║     ██║  ██║╚██████╔╝ ╚████╔╝ ███████╗       ██║   ╚██████╔╝╚██████╔╝    ╚██████╗██║  ██║██║ ╚████║    ██████╔╝███████╗██║  ██║   ██║   
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝   ╚═══╝  ╚══════╝       ╚═╝    ╚═════╝  ╚═════╝      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   
                                                                                                                                                
                                                             ██████╗ ███╗   ██╗██╗███████╗██╗                                                   
                                                            ██╔════╝ ████╗  ██║██║╚══███╔╝██║                                                   
                                                            ██║  ███╗██╔██╗ ██║██║  ███╔╝ ██║                                                   
                                                            ██║   ██║██║╚██╗██║██║ ███╔╝  ██║                                                   
                                                            ╚██████╔╝██║ ╚████║██║███████╗██║                                                   
                                                             ╚═════╝ ╚═╝  ╚═══╝╚═╝╚══════╝╚═╝                                                                                                                                                                                               
    Menu:
    1. Start
    2. Exit""")

    choice = input('What\'s  your choice? ')

    if choice != '1' and choice != '2':
        print("Wrong input, get out of this class!")
        exit()

    {'1': game,
     '2': exit_func}[choice]()


if __name__ == "__main__":
    main()
