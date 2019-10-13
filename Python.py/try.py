def students_names(grade):
    names=list(grade.keys())
    return names
def students_score(grade,name):
    score=sum(grade[name])
    return score
def students_count(grade):
    names=list(grade.keys())
    count=len(names)
    return count
grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7], 'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}

grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}

grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9], 'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}
while True:
    a=input("Choose one: students_names, student_score, students_count: ")
    if a=='students_names':
        b=input("grade: ")
        if b=="grade_one":
            print(students_names(grade_one))
        elif b=="grade_two":
            print(students_names(grade_two))
        elif b=="grade_three":
            print(students_names(grade_three))
        else:
            print('not exist')
    elif a=='students_score':
        b=input("grade: ")
        c=input("student name: ")
        if b=="grade_one":
            print(students_score(grade_one,c))
        elif b=="grade_two":
            print(students_score(grade_two,c))
        elif b=="grade_three":
            print(students_score(grade_three,c))
        else:
            print('not exist')
    elif a=='students_count':
        b=input("grade: ")
        if b=="grade_one":
            print(students_count(grade_one))
        elif b=="grade_two":
            print(students_count(grade_two))
        elif b=="grade_three":
            print(students_count(grade_three))
        else:
            print('not exist')
    d=input('Done Or More?')
    if d=='Done':
        break
