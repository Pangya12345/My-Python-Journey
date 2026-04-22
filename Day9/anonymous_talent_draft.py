print("Welcome to the Talent draft generator!")
talent = {}
def find_talent(real_talent):
    top_talent_draft = 0
    top_talent_person = ""
    for name in real_talent:
        if real_talent[name] > top_talent_draft:
            top_talent_draft = real_talent[name]
            top_talent_person = name
    print(f"The winner is {top_talent_person} with the highest talent score of {top_talent_draft}")


stop = False
while not stop:
    name = input("What is your name? ")
    skill = int(input("What is your skill level (0 - 100) "))
    experience = int(input("How many year of your experience? "))
    any_person = input("Are there any person in the talent draft? type 'yes' or 'no' ").lower()
    if 0 > skill > 100:
        stop = True
        print("You put the invalid skill level! Start the program again!")
    elif any_person == "yes":
        print("\n" * 100)
    def calculate_talent_score(real_skill, real_experience):
        talent_score = real_skill + (real_experience * 3)
        return talent_score
    talent[name] = calculate_talent_score(skill, experience)
    if any_person == "no":
        stop = True
        find_talent(talent)





