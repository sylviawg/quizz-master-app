from question_model import Question
from data import get_question_data
from quiz_brain import QuizBrain

from ui import QuizInterface

def create_quiz():
    """Create a new QuizBrain instance containing fresh quiz questions."""

    question_data = get_question_data()

    question_bank = []

    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]

        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    return QuizBrain(question_bank)


quiz = create_quiz()

quiz_interface = QuizInterface(quiz, create_quiz)

