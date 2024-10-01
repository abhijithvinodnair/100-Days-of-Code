class QuizBrain():
    def __init__(self,list):
        self.number = 0
        self.list = list
        self.score = 0

    def still_has_questions(self):
        return self.number < len(self.list)
    def next_question(self):
        current_question = self.list[self.number]
        self.number += 1
        user_input = input(f"Q.{self.number}: {current_question.text} (True/False):")
        self.check_answer(user_input, current_question.answer)
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it!")
            self.score += 1
        else:
            print("Oh no. That's wrong")
            print(f"The correct answer was:{correct_answer}")
        print(f"Your current score = ({self.score})/({self.number})")
        print()








