from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []  # question bank list

# loop through question_data dictionary list
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    # creating a question objects with required attribute
    new_question = Question(question_text, question_answer)
    # adding the object in the question_bank list
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
    print()

print("You have completed the quiz!")
print(f"Your Final score is: {quiz.score}/{quiz.question_number}")
