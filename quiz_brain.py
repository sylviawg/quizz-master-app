import html

class QuizBrain:
    """
    Manages the quiz logic, including questions, scoring,
    and moving through the quiz.
    """
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """
        Checks if there are still more questions by comparing the current question number
        against the total number of questions.
        Returns 'True' if the current question number is lower than the total number of questions.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Retrieves the next question and updates the question number.
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"


    def check_answer(self, user_answer):
        """
        Checks the users input against the correct answer of the question.
        Returns True if the user has answered correctly.
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

