import re

from question import Question
from input import InputReader
from parser import Parser

def get_user_input():
    user_input = input("Your answer [a|b|c]: ").strip().lower()
    return user_input

input_reader = InputReader()
extracted_text = input_reader.read_file()
details = input_reader.extract_details(extracted_text)

parser = Parser(details)
parsed_data = parser.parse()

questions = []
for question in parsed_data:
    questions.append(Question(question['question'], [a['answer'] for a in question['answers']], next((a['answer'] for a in question['answers'] if a['correct']), None)))


for question in questions:

    question.display_question()
    user_answer = get_user_input()
    
    while not question.check_answer(user_answer):
        print("\nIncorrect!\n")
        question.display_question()
        user_answer = get_user_input()

    print("\nCorrect!\n")

    # if not question.check_answer(user_answer):
    #     print("Correct!")
    # else: