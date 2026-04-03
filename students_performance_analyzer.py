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


with open("students.csv", "r")as file:
    next(file)
    for line in file:
        student = [item.strip() for item in line.strip().split(",")]
        name = student[0]
        marks = list(map(int, student[1:]))
        avg = calculate_average(marks)
        grade = calculate_grade(avg)
        
        if avg > top_avg:
            top_avg = avg
            top_name = name
            
        if avg < low_avg:
            low_avg = avg
            low_name = name
            
        print(f"{name.capitalize()} → Avg: {avg:.1f} → {grade}")

print("\nFinal Result:")
print(f"Topper: {top_name.capitalize()} ({top_avg:.1f})")
print(f"Lowest: {low_name.capitalize()} ({low_avg:.1f})")