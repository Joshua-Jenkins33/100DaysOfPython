from question_model import Question
# from data import question_data
from data1 import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    # question_bank.append(Question(question['text'], question['answer'])) # you should simplify this
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[0].answer)

quiz = QuizBrain(question_bank) 

# print(len(question_bank))

# while: #if quiz still has questions remaining
#     quiz.next_question()

while quiz.still_has_questions() == True:
    quiz.next_question()


print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")