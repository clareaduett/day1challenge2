#Compute the age
def age():
    yob=int(input('Enter year of birth: '))
    current_year=2018
    age= current_year - yob
    print(age)
    
 #Given the age,
    if age < 18:
        print('Minor')
    elif age >= 18 and age <= 36:
        print('Youth')
    else:
        print('Elder')
age()
