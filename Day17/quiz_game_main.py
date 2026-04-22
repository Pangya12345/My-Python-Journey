# From quiz_brain file, we import Quiz
from quiz_brain import Quiz
car = Quiz()
# Split only the question from question_data and add to new list
car.text_split_function()
# Split only the answer from question data and add to the new list
car.answer_split_function()
# Set up the game loop
while car.question_round < len(car.text_list):
# display the question (game logic)
    car.question_display()
# Show final score
car.complete()
