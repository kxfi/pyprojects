from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [] # list of question objects 

# converting text value to string
# converting answer value to string

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer) # make question object
    question_bank.append(new_question) 


quiz = QuizBrain(question_bank)
quiz.next_question() # First Question


while quiz.still_has_questions(): # if quiz still has questions remaining loops until end
    quiz.next_question() # and ends

# When done with
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


