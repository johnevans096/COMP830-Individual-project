def answerYes():
    print("Woohoo! I guessed it! Try again?")
    answer = input().lower()

    if answer == "yes":
        design_pattern_game()
    else:
        endGame()

def answerNo():
    print("Oops! Something went wrong! Try again?")
    design_pattern_game()

def showQuestion(question):
    print(question)
    answer = input().lower()

    if answer == "yes":
        return True
    elif answer == "no":
        return False
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")
        return showQuestion(question)

def endGame():
    print("End")

def design_pattern_game():
    print("Welcome to the game! Think of a design pattern and answer the following yes/no questions. Ready?")
    answer = input().lower()

    if answer == "yes":
        if showQuestion("Does it provide the object creation mechanism that enhances the flexibilities of the existing code?"):
            if showQuestion("Does it ensure you have at most one instance of a class in your application?"):
                if showQuestion("Is it Singleton Pattern?"):
                    answerYes()
                else:
                    answerNo()
            else:
                if showQuestion("Is it Builder Pattern?"):
                    answerYes()
                else:
                    answerNo()
        else:
            if showQuestion("Is it responsible for how one class communicates with others?"):
                if showQuestion("Does it provide a mechanism for the context to change its behavior?"):
                    if showQuestion("Is changing behavior built into its scheme?"):
                        if showQuestion("Is it State Pattern?"):
                            answerYes()
                        else:
                            answerNo()
                    else:
                        if showQuestion("Is it Strategy Pattern?"):
                            answerYes()
                        else:
                            answerNo()
                else:
                    if showQuestion("Does it allow a group of objects to be notified when some state changes?"):
                        if showQuestion("Is it Observer Pattern?"):
                            answerYes()
                        else:
                            answerNo()
                    else:
                        if showQuestion("Is it Command Pattern?"):
                            answerYes()
    else:
        endGame()

def main():
    design_pattern_game()

if __name__ == "__main__":
    main()
