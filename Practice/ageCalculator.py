import re
dob = input("Enter your date of birth in mm/dd/yyyy format: ")
pattern = re.compile('\d{4}[-/]\d{2}[-/]\d{2}')


'''
def ageCalculator(y,m,d):
    import datetime
    today = datetime.datetime.now().date()
    dob = date(y,m,d)
    age = int((today-dob).days / 365.25)
    print("Age: ",age)
ageCalculator
'''