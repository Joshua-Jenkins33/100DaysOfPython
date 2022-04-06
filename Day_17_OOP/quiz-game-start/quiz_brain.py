#TODO: Asking the questions
#TODO: Checking if the answer was correct
#TODO: Checking if we're at the end of the quiz

# attributes: 
## question_number = 0 # calculates which question we're on
## questions_list

# methods
## nextquestion()

# display the question number (Q.#)
# displays the question text
# displays (True/False)

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        """
        Return a boolean depending on the value of question_number.
        Use the while loop to show the next question until the end
        """
        return self.question_number < len(self.question_list)
        #     return False
        # else:
        #     return True

    def next_question(self):
        """
        Retreive the item at the current question_number from the question_list
        Use the input() function to show the user the Question text and ask for the user's answer
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")   
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        print(f"The answer was {correct_answer.lower()}")
        
        if user_answer.lower() == correct_answer.lower():
            print("Well done, you were right!")
            self.score += 1
        else:
            print("Bummer. That's wrong.")

        print(f"You're current score is: {self.score}/{self.question_number}")
        print('\n')
