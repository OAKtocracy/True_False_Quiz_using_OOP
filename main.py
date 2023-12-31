from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []

for item in question_data:
    question_text = item['question']
    question_answer = item['correct_answer']
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()


print('You have completed the quiz')
print(f'Your final score was: {quiz.score}/{len(question_bank)}')