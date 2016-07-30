grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
print "Grades:", grades

#prints each number in the sequence of grades. 
def print_grades(grades): 
    for num in grades: 
        print num

#returns the total of graded exams. 
def grades_sum(scores):
    total = 0 
    for grades in scores: 
        total += grades
    return total 

#return the average of the total graded exams. 
def grades_average(grades):
    return grades_sum(grades) / float(len(grades))

#computes the variance. 
def grades_variance(scores): 
    average = grades_average(scores)
    variance = 0 
    for score in scores:
        difference = (average - score)**2
        variance += difference
        new_variance = variance / float(len(scores))
    return new_variance

def grades_std_deviation(variance): 
    return variance**0.5


