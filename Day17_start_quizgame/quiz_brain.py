# questioning and quizzing
#TODO:asking the questions
#TODO: checking if the answer was correct
#TODO: checking if we're the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list # the whole question bank (list) received
        self.score = 0
        # questions_list use number to go through list of questions passed to brain object initialization

    def still_has_questions(self): # boolean
        return self.question_number < len(self.question_list) # automatically True ot false

    def next_question(self): # dont need to question pass through
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False) ") # not in variable, current_question.text
        self.check_answer(user_answer, current_question.answer) # Question object with self.text and self.answer attributes
    # CAN TAP INTO OTHER METHODS THAT ARE NOT CALLED IN MAIN

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong.")

        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
        print()

