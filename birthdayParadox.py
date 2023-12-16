import random
import datetime

def getBirthdays(noOfBirthdays):
    """Returns a list of random date object that only hold 
    the month and day for birthdays"""

    birthdays = []
    months = ('Jan','Feb','March','April','May','June','July',
              'August','Sept','Oct','Nov','Dec')
    #The year is unimportant for our simulation, as longs as 
    # all birthdays have the same 
    startOfYear = datetime.date(2023,1,1) 

    for _ in range(noOfBirthdays):
        #get random day into the year
        birthdate = startOfYear + datetime.timedelta(random.randint(0,364))
        #concatenate month and day to get single date
        #use the month tuple to convert the months from interger to Name
        birthdays.append(str(months[birthdate.month-1]) +' '+ str(birthdate.day))

    return birthdays


def getMatch(birthdays):
    """Returns the date object that occurs more than once in the birthday list"""
    uniqueDates = set()

    if len(set(birthdays)) == len(birthdays):
        return None
    for date in birthdays:
        if date not in uniqueDates:
            uniqueDates.add(date)
        else:
            return date
        
        
def getMatch1(birthdays):
    """Does the same things as the first getMatch function, 
    it's implemented in a slightly different way"""
    if len(set(birthdays)) == len(birthdays):
        return None
    for a, birthdayA in enumerate(birthdays):
        for _,birthdayB in enumerate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA


if __name__ == "__main__":
    print('''Birthday Paradox, by Al Sweigart.

    The Birthday Paradox shows us that in a group of N people, the odds
    that two of them have matching birthdays is suprisingly large.
    This program does a Monte Carlo simiulation (that is, repeated random simulation)
    to explore this concept.

    (Its's not actually a paradox, it's just a suprising result.)
    ''')
    print()
    print('How many Birthdays shall i generate. (Max 100)')
    noOfBirthdays = input('>')

    while  not noOfBirthdays.isdecimal() or not (0 < int(noOfBirthdays) <=100):
        print('Enter a value within range')
        noOfBirthdays = input('>')
    
    print()
    print(f"Here are, {noOfBirthdays} birthdays:")
    #Convert the variable noOfBirthdays from string to interger to be used 
    #in the getBirthdays function.
    birthdays = getBirthdays(int(noOfBirthdays))
    print(', '.join(birthdays))
    print()
    print()
    

    #Determine if there are two birthdays that match.
    match = getMatch(birthdays)
    print("In this simulation, ", end='')
    if match == None:
        print("There are no matching birthdays.")
    else:
        print(f'Multiple people have a birthday on {match}.')
    print()

    #Run through 100,000 simulations:
    print(f"Generating {noOfBirthdays} random birthdays 100,000 times...")
    input("Press Enter to begin...")

    print("Let's run another 100,000 simulations.")
    matchesCounted = 0 #How many simulations have matching birthdays in them 
    for i in range(100000):
        if i % 10000 == 0:
            print(f'{i} simulations run...')
        birthdays = getBirthdays(int(noOfBirthdays))
       
        if getMatch(birthdays) != None:
            matchesCounted += 1

    print('100,000 simulations run.')

    #Display simulation results
    probability = round(matchesCounted/100000 *100,2)
    print(f'''Out of 100,000 simulations of {noOfBirthdays} people there was a
    matching birthday in that group {matchesCounted} times. This means
    that {noOfBirthdays} people have a {probability}% chance of
    having a matching birthday in their group.
    That's probably more than you'd think!''')

   