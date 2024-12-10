



def grade_one(score, best_score):
    if score >= best_score - 10:
        return 'A'
    elif score >= best_score - 20:
        return 'B'
    elif score >= best_score - 30:
        return 'C'
    elif score >= best_score - 40:
        return 'D'
    else:
        return 'F'


def grade_many(scores):
    best_score = max(scores)
    grades = {}
    for score in set(scores):
        grades[score] = grade_one(score,best_score)
    return grades



def main():
    # assuming they will input an int
    num = int(input('Total number of students:'))
    while True:
        # the scores will still be type string
        str_scores = (input(f'Enter {num} score(s):')).split()
        if len(str_scores) < num:
            continue
        else: # len(str_scores) >= num
            str_scores = str_scores[:num] # only consider first num elements
            break
    scores = [int(x) for x in str_scores]
    #
    score_grade_pairs = grade_many(scores)
    for i in range(num):
        (s_num, score, letter) = (i+1, scores[i], score_grade_pairs[scores[i]])
        print(f'Student {s_num} score is {score} and grade is {letter}')



main()
