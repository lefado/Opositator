import re

class Parser:
    def __init__(self, details):
        self.details = details
        self.questions = []
        self.answers = []
        self.correct_answers = []

    def parse(self):
        previous_line = None
        for line in self.details:
            if bool(re.match(r'^\d+\. ', line)):
                self.questions.append(line)
            elif bool(re.match(r'^[a-c]\)', line)):
                self.answers.append(line)
            # Sometimes there are \n between questions or answer. They need to get appended to previous text
            else:
                if bool(re.match(r'^\d+\. ', previous_line)):
                    self.questions[-1] = self.questions[-1] + ' ' + line
                elif bool(re.match(r'^[a-c]\)', previous_line)):
                    self.answers[-1] = self.answers[-1] + ' ' + line
            previous_line = line

        answers_groups = self.group_into_chunks(self.answers, 3)
        final_questions = []

        for i in range(len(self.questions)):
            final_answers = []
            question = self.questions[i]
            answers_group = answers_groups[i]

            for ans in answers_group:
                if bool(re.match(r'.*£', ans)):
                    final_answers.append({'answer': ans.replace(' £', ''), 'correct': True})
                else:
                    final_answers.append({'answer': ans, 'correct': False})

            final_questions.append({'question': question, 'answers': final_answers})

        return final_questions

    def group_into_chunks(self, lst, chunk_size):
        return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
