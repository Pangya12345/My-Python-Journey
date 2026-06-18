import random
while True:
  level = input("Level: ")
  if level.isalpha():
    continue

  elif level.isdigit():
    if int(level) <= 0:
      continue

    else:
      doing = int(level)
      correct_number = random.randint(1, doing)
      break

while True:
  guess = input("Guess: ")
  if guess.isalpha():
    continue

  elif guess.isdigit():
    formatting = int(guess)

    if formatting <= 0:
      continue

    elif formatting > correct_number:
      print("Too large!")

    elif formatting < correct_number:
      print("Too small!")

    elif formatting == correct_number:
      print("Just right!")
      break








  



