import random
import datetime

def getBirthdays(noOfBirthdays):
    """Returns a list of random date object that only hold 
    the month and day for birthdays"""

    birthdays = []
    months = ('Jan','Feb','March','April','May','June','July','August','Sept','Oct','Nov','Dec')
    #The year is unimportant for our simulation, as longs as 
    # all birthdays have the same 
    startOfYear = datetime.date(2023,1,1) 

    for _ in range(noOfBirthdays):
        #get random day into the year
        birthdate = startOfYear + datetime.timedelta(random.randint(0,364))
        #concatenate month and day to get single date
        #use the month tuple to convert the months from interger to Name
        birthdays.append(str(months[birthdate.month-1]) +' '+ str(birthdate.day))

    #printing the list of birthdays as a single string
    print(', '.join(birthdays))
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
    print('Enter the number of birthday to generate. (Max 100)')
    noOfBirthdays = input('>')

    while  not noOfBirthdays.isdecimal() or not (0 < int(noOfBirthdays) <=100):
        print('Enter a value within range')
        noOfBirthdays = input('>')
   
    print(getMatch1(getBirthdays(int(noOfBirthdays))))
