from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    n_question = Question(text = question_text, answer= question_answer)
    question_bank.append(n_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()



print("That's the end of the quiz")
print(f"Thanks for playing. Your final score = {quiz.score}/{quiz.number}")
