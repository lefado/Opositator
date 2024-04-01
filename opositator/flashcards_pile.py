import re
import csv

class FlashcardsPile:
    '''
    Manages parsed data from test exam and converts them to Anki flashcards format.
    '''
    def __init__(self, parsed_data) -> None:
        self.flashcards = self.add_style(parsed_data)

    def add_style(self, parsed_data: list[dict]) -> list[tuple]:
        '''
        Add html style to questions and answers.
        Format into tuples of strings (full_question, answer).
        '''
        flashcards = []
        for final_question in parsed_data:
            flashcard_face = f"<strong>{final_question['question']}</strong>"
            for answer in final_question["answers"]:
                flashcard_face += f"<br>{answer['answer']}"
                if answer["correct"]:
                    flashcard_back = f"<big>{answer['answer']}</big>"
            flashcards.append((flashcard_face, flashcard_back))
        return flashcards

    def matches_pattern(self, flashcard: tuple[str, str]) -> bool:
        '''
        Checks if a specific flashcard matches expected pattern.
        '''
        pattern = r'\<strong\>\d+..+a\).+b\).+c\).+[a-c]\)'
        flashcard = flashcard[0] + flashcard[1].strip()
        if re.match(pattern, flashcard.strip(), flags=re.DOTALL):
            return True
        else:
            return False

    def sanity_check(self) -> None:
        '''
        Checks matching pattern for every question in the set printing errors
        and error count and question count.
        '''
        failed_questions = 0
        for question_with_answer in self.flashcards:
            try:
                if not self.matches_pattern(question_with_answer):
                    failed_questions += 1
                    print("#### Prueba no pasada")
                    print(question_with_answer)
            except Exception as e:
                print(f"ERROR: {e}\n\n{question_with_answer}")
        print("Number of questions:", len(self.flashcards))
        print("Questions with errors:", failed_questions)

    def to_csv(self, filename: str = None):
        '''
        Export flashcards to csv so they can be imported in Anki.
        '''
        if not filename:
            filename = "anki_flashcards.csv"
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Question with Options', 'Answer'])
            writer.writerows(self.flashcards)
        print(f"Flashcards writen to {filename}")
