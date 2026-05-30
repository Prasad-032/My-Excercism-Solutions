def round_scores(student_scores):
    return [round(score) for score in student_scores]

def count_failed_students(student_scores):
    count = 0
    for score in student_scores:
        if score <= 40:
            count += 1
    return count

def above_threshold(student_scores, threshold):
    return [score for score in student_scores if score >= threshold]

def letter_grades(highest):
    increment = (highest - 40) //4
    return [41 + increment * i for i in range(4)]

def student_ranking(student_scores, student_names):
    result =[]
    for index, name in enumerate(student_names):
        rank = index + 1
        score = student_scores[index]
        result.append(f"{rank}. {name}: {score}")
    return result

def perfect_score(student_info):
    for student in student_info:
        if student[1] == 100:
            return student
    return []
        
    