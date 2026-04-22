# Import question_data from data to sue in this file
from Data import question_data
# Define the class Quiz
class Quiz:
# Define the attribute
    def __init__(self):
        self.question_round = 0
        self.question_number = 0
        self.text_list = []
        self.answer_list = []
        self.current_score = 0
        self.current_score_correct = 0
# add all of the questions into 'text_list'
    def text_split_function(self):
        for question in question_data:
            self.question_number += 1
            self.text_list.append(f"Q.{self.question_number}: {question["text"]} (True/False)")
# Add answers of that question into 'answer_list'
    def answer_split_function(self):
        for answer in question_data:
            self.answer_list.append(answer["answer"])
# display the score when player make the right choice
    def right_count(self):
        self.current_score += 1
        self.current_score_correct += 1
        print(f"Your current score is: {self.current_score_correct}/{self.current_score}")
# display the score when play make the wrong choice
    def wrong_count(self):
        self.current_score += 1
        print(f"your current score is: {self.current_score_correct}/{self.current_score}")
# Display the final score when the game is finish
    def complete(self):
        print("You completed the quiz!")
        print(f"Your final score is {self.current_score_correct}/{self.current_score}")
# display the question for each round
    def question_display(self):
        question = input(f"{self.text_list[self.question_round]} ").capitalize()
        if question == self.answer_list[self.question_round]:
            print("You got it right!")
            print(f"The correct answer was: {self.answer_list[self.question_round]}")
            self.right_count()
            print("\n")
        else:
            print("That's wrong")
            print(f"The correct answer was: {self.answer_list[self.question_round]}")
            self.wrong_count()
            print("\n")
        self.question_round = self.question_round + 1


