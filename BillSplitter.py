# Jetbrains Academy. 
# Project: Bill Splitter

import random

no_people = int(input("How many people want to join us: \n"))

if(no_people <= 0):
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    names = {input(): 0 for i in range(no_people)}
    bill = int(input("\nEnter the total bill value: \n"))
    

    
    option = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No: \n')
    
    if(option == 'Yes'):
        x = [i for i in names.keys()]
        lucky = random.choice(x)
        per_person = round(bill/(no_people-1), 2)
        for i in names:
            names[i] = per_person
        names[lucky] = 0
        print(lucky, "is the lucky one!\n")
        print(names)
    else:
        per_person = round(bill/no_people, 2)
        for i in names:
            names[i] = per_person
        print("\nNo one is going to be lucky")
        print(names)
