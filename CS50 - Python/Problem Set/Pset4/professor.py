import random
question_list = []
number_list = ["1", "2", "3"]

while True:
  level = input("Level: ")
  if level in number_list:
    real_level = int(level)
    break
  else:
    continue


number_1 = "0"
number_2 = "9"

def compare(num_1, num_2, evel):
  if evel == 1:
    numb_1 = int(num_1)
  
  elif evel == 2:
    numb_1 = int("1" + num_1)
  
  else:
    numb_1 = int("1" + num_1 * 2)

  numb_2 = int(num_2 * evel)
  return numb_1, numb_2

zombie_1, zombie_2 = compare(number_1, number_2, real_level)
    



def adjustment(n_1, n_2, q_list):
    for t in range(10):
      x = str(random.randint(n_1, n_2))
      y = str(random.randint(n_1, n_2))
      q_list.append(x + " " + "+" + " " + y + " " + "=" + " ")
adjustment(zombie_1, zombie_2, question_list)


score = 0

while len(question_list) == 10:
  corn = question_list.pop()
  gun = input(corn )
  