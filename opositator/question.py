class Question:
    def __init__(self, question_text, answers, correct_answer):
        self.question_text = question_text
        self.answers = answers
        self.correct_answer = correct_answer

    def display_question(self):
        print('\n'+self.question_text + '\n')
        for idx, answer in enumerate(self.answers, start=1):
            print(f"{answer}")

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer[0]