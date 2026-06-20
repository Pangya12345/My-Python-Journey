import random

question_list = []
number_list = ["1", "2", "3"]

while True:
    level = input("Level: ")
    if level in number_list:
        real_level = int(level)
        break
    else:
        continueS

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

while len(question_list) > 0:
    corn = question_list.pop(0)
    gun = input(corn)

    def get_answer(le):
        if le == 1:
            mama_1 = int(corn[0])
            mama_2 = int(corn[4])
        elif le == 2:
            mama_1 = int(corn[0] + corn[1])
            mama_2 = int(corn[5] + corn[6])
        else:
            mama_1 = int(corn[0] + corn[1] + corn[2])
            mama_2 = int(corn[6] + corn[7] + corn[8])

        result = mama_1 + mama_2
        return result

    if int(gun) != get_answer(real_level):
        print("EEE")
        count = 1
        while True:
            gun = input(corn)
            if int(gun) == get_answer(real_level):
                break
            else:
                print("EEE")
                count = count + 1
                if count == 3:
                    print(corn + str(get_answer(real_level)))
                    break
    else:
        score += 1

print(f"Score: {score}")
