def gradingStudents(grades):
    # Write your code here
    for i in grades:
        if i >=38:
            for j in range(i, i+3):
                if j%5 == 0:
                   grades[grades.index(i)] = j
        else:
            continue            
    return grades