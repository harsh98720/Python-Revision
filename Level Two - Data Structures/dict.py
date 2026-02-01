# Dictionary:
# student marks dict → topper find

students_marks = {
    "Aman": 378,
    "Rohit": 425,
    "Neha": 462,
    "Priya": 441,
    "Rahul": 356,
    "Simran": 480,
    "Karan": 312,
    "Anjali": 398,
    "Vikas": 289,
    "Pooja": 491
}

topper_marks = 0
topper = ""

for key in students_marks :
    if students_marks[key] > topper_marks:
        topper_marks = students_marks[key]
        topper = key

print(f"{topper} topped with {topper_marks} marks")

# average

total_marks = 0
count = 0

for key in students_marks :
    total_marks += students_marks[key]
    count += 1

average = round(total_marks/count)
print(average)