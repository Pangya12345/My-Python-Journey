ืRune_magical = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
ancient_number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
Forbidden_symbol = ["@", "#", "$", "*", "&"]

nr_Rune_magical = int(input("How many Rune letter would you like to have on your spell?"))
nr_ancient_number = int(input("How many ancient number would you like to have on your spell?"))
nr_Forbidden_symbol = int(input("How many forbidden_symbol would you like to have on your spell?"))

import random

spell_list = []
for magic in range(nr_Rune_magical):
    spell_list.append(Rune_magical[magic])

for magic in range(nr_ancient_number):
    spell_list.append(ancient_number[magic])

for magic in range(nr_Forbidden_symbol):
    spell_list.append(Forbidden_symbol[magic])

random.shuffle(spell_list)

spell = ""
for chat in spell_list:
    spell += chat
print(f"You dragon spell is: {spell}")
Rune_magical = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
ancient_number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
Forbidden_symbol = ["@", "#", "$", "*", "&"]

nr_Rune_magical = int(input("How many Rune letter would you like to have on your spell?"))
nr_ancient_number = int(input("How many ancient number would you like to have on your spell?"))
nr_Forbidden_symbol = int(input("How many forbidden_symbol would you like to have on your spell?"))

import random

spell_list = []
for magic in range(nr_Rune_magical):
    spell_list.append(Rune_magical[magic])

for magic in range(nr_ancient_number):
    spell_list.append(ancient_number[magic])

for magic in range(nr_Forbidden_symbol):
    spell_list.append(Forbidden_symbol[magic])

random.shuffle(spell_list)

spell = ""
for chat in spell_list:
    spell += chat
print(f"You dragon spell is: {spell}")
Rune_magical = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
ancient_number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
Forbidden_symbol = ["@", "#", "$", "*", "&"]

nr_Rune_magical = int(input("How many Rune letter would you like to have on your spell?"))
nr_ancient_number = int(input("How many ancient number would you like to have on your spell?"))
nr_Forbidden_symbol = int(input("How many forbidden_symbol would you like to have on your spell?"))

import random

spell_list = []
for magic in range(nr_Rune_magical):
    spell_list.append(Rune_magical[magic])

for magic in range(nr_ancient_number):
    spell_list.append(ancient_number[magic])

for magic in range(nr_Forbidden_symbol):
    spell_list.append(Forbidden_symbol[magic])

random.shuffle(spell_list)

spell = ""
for chat in spell_list:
    spell += chat
print(f"You dragon spell is: {spell}")
