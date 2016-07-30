grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
print "Grades:", grades

#prints each number in the sequence of grades. 
def print_grades(grades): 
    for num in grades: 
        print num

print "Let's compute some stats!"

#returns the total of graded exams. 
def grades_sum(scores):
    total = 0 
    for grades in scores: 
        total += grades
    return total 

