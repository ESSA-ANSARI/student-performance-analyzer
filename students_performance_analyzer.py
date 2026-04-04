def calculate_average(marks):
    return sum(marks) / len(marks)

def calculate_grade(avg):
    if avg >= 90:
        return "Grade: A+"
    elif avg >= 80:
        return "Grade: A"
    elif avg >= 70:
        return "Grade: B+"
    elif avg >= 60:
        return "Grade: B"
    elif avg >= 50:
        return "Grade: C"
    elif avg >= 40:
        return "Grade: D"
    else:
        return "Grade: F"

top_avg = 0
top_name = ""

low_avg = 100
low_name = ""

averages = []
student_data = []

subject1_topper = 0
subject1_name = ""

subject2_topper = 0
subject2_name = ""

subject3_topper = 0
subject3_name = ""

subject4_topper = 0
subject4_name = ""

subject5_topper = 0
subject5_name = ""



with open("students.csv", "r")as file:
    next(file)
    for line in file:
        student = [item.strip() for item in line.strip().split(",")]
        name = student[0]
        marks = list(map(int, student[1:]))
        avg = calculate_average(marks)
        grade = calculate_grade(avg)
                        
        averages.append(avg)
        student_data.append((name, avg))
            
        if avg > top_avg:
            top_avg = avg
            top_name = name
            
        if avg < low_avg:
            low_avg = avg
            low_name = name
        
        if marks[0] > subject1_topper:
            subject1_topper = marks[0] 
            subject1_name = name
            
        if marks[1] > subject2_topper:
            subject2_topper = marks[1]
            subject2_name = name
        
        if marks[2] > subject3_topper:
            subject3_topper = marks[2]
            subject3_name = name
        
        if marks[3] > subject4_topper:
            subject4_topper = marks[3]
            subject4_name = name
            
        if marks[4] > subject5_topper:
            subject5_topper = marks[4]
            subject5_name = name
            
        print(f"{name.capitalize()} → Avg: {avg:.1f} → {grade}")

class_average = sum(averages) / len(averages)
sorted_student = sorted(student_data, key=lambda x:x[1], reverse=True)
print("\nFinal Result:")
print(f"Topper: {top_name.capitalize()} ({top_avg:.1f})")
print(f"Lowest: {low_name.capitalize()} ({low_avg:.1f})")
print(f"Class Average: ({class_average:.1f})")
print("\n-----Ranking-----")
rank = 1
for student in sorted_student:
    print(f"{rank}. {student[0].capitalize()} → {student[1]:.1f}")
    rank += 1
print("\n------- SUBJECT TOPPERS -------")
print(f"Subject 1 Topper : {subject1_name.capitalize()} ({subject1_topper})")
print(f"Subject 2 Topper : {subject2_name.capitalize()} ({subject2_topper})")
print(f"Subject 3 Topper : {subject3_name.capitalize()} ({subject3_topper})")
print(f"Subject 4 Topper : {subject4_name.capitalize()} ({subject4_topper})")
print(f"Subject 5 Topper : {subject5_name.capitalize()} ({subject5_topper})")
