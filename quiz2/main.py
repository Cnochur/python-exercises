from quiz import Quiz

if __name__ == "__main__":
    print("\n_=_= T-Quizzil =_=_")
    name = input("\n\nEnter your name: ")

    while True:
        quiz = Quiz(name)
        quiz.quiz_menu()
