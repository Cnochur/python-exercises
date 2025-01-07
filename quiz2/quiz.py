from quiz_api import QuizAPI

class Quiz:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.quiz_api = QuizAPI()

    def quiz_menu(self):
        print("\n_=_= Quizz Menu =_=_")

        try:
            print("\n1) Linux\n2) Code\n3) Django\n4) Random\n5) Exit")
            choice = int(input("\n\nEnter: "))

            if choice == 1:
                self.start_quiz("Linux")  # Fetch Linux questions
            elif choice == 2:
                self.start_quiz("Code")  # Fetch Python questions
            elif choice == 3:
                self.start_quiz("Django")  # Fetch CyberSec questions
            elif choice == 4:
                self.start_quiz("uncategorized")  # Mega-Quiz as a general quiz
            elif choice == 5:
                print("\n....Goodbye!!\n")
                quit()
        except ValueError:
            print("Error, choose: 1, 2, 3, 4, or 5.")

    def start_quiz(self, category):
        print(f"\nStarting quiz on {category}...")

        questions = self.quiz_api.fetch_questions(category)

        if not questions:
            print(f"No questions found for category: {category}")
            return

        for index, question in enumerate(questions, start=1):
            print(f"\n{index}. {question['question']}\n")

            answers = question['answers']
            correct_answer_key = None

            available_answers = {}
            answer_index = 1  # Start answer index from 1
            for ind, answer in answers.items():
                if answer != None:  # Skip invalid answers
                    available_answers[answer_index] = answer
                    print(f"\t\t{answer_index}) {answer}")
                    answer_index += 1


            correct_answers = question["correct_answers"]
            
            #print(correct_answers)

            '''correct_answers is a dict. After chatGPT and google i was lost. 
            Looking at the keys in correct_answers made me realise in order to do this 
            i would need to append the correct_answers values to the respective available_answers item.

            maybe merge then to a list: 

                    new_question_list = [(q1,[a1,a2,a3,a4],a1), (q2,[a1,a2,a3,a4],a3)]

            this way i could then maybe compare the user input eg:

                    user_input = 1
                    correct_answer = new_question_list[2]:
                    if user_input == correct_answer:
                        correct
            
            ''' 
            for key, value in correct_answers.items():
                if value == "true":
                    correct_answer_key = key

            if correct_answer_key:
                correct_answer = answers[correct_answer_key.replace("_correct", "")]

                try:
                    user_choice = int(input("\nEnter your answer: "))
                    if available_answers.get(user_choice) == correct_answer:
                        self.score += 1
                        print("\nCorrect!")
                    else:
                        print("Incorrect!")
                except KeyError:
                    print("Invalid answer choice!")

        print(f"\n{self.name}, you have scored: {self.score} / {len(questions)}")
