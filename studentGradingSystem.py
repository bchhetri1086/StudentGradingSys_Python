import statistics

admins = {'Bhuban':'Pass123','secondUser':'e2etesting'}

studentDict = {'Jeff':[89,98,99],
               'Rasta':[99,99,93],
               'Safari':[56,98,201]
               }


def enterGrades():
    nameToEnter = input('Student Name: ')
    gradeToEnter = input('Grade: ')
    
    if nameToEnter in studentDict:
        print('Adding Grade...')
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('Student not available for grading.')
    print(studentDict)   

    
    
def removeStudent():
    nameToRemove = input('which student to remove?: ')
    if nameToRemove in studentDict:
        print('Removing Student...', nameToRemove)
        del studentDict[nameToRemove]
    else:
        print('Student not found', nameToRemove)
        
    print(studentDict)    
    
    
def main():
    print("""
    Welcome to Grading System - By Bhuban
    
    [1]  - Enter Grades
    [2]  - Remove Student
    [3]  - Student Average Grades
    [4]  - Exit
    """)
    
    
    action = input('Please Choose an option. (Enter a Number) ')
    
    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        print ('3')
    elif action == '4':
        exit()
    else:
        print ('Invalid Option please try again')

login = input('Username: ') 
Pwd = input ('Password: ')

if login in admins:
    if admins[login] == Pwd:
        print('Login Success,',login)   
        while True:   
            main()
    else:
        print('Invalid Password, Kaboom in 5 sec...1...2...3...4...KABOOOOOOM')
else:
    print('Invalid username, you failed')
