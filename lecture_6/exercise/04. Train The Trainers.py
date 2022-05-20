number_of_people = int(input())
name_of_presentation = input()
counter = 0
sum_grade = 0
sum_all_presentations = 0
while name_of_presentation != "Finish":
    sum_grade = 0
    for x in range(number_of_people):
        grade = float(input())
        sum_grade += grade
    average_grade = sum_grade / number_of_people
    print(f"{name_of_presentation} - {average_grade:.2f}.")
    counter += 1
    sum_all_presentations += average_grade
    name_of_presentation = input()
average_grade_all_presentations = sum_all_presentations / counter
print(f"Student's final assessment is {average_grade_all_presentations:.2f}.")
