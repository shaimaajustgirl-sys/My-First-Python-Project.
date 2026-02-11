print("Hello from my first project on GitHub!")
print("I am a future IT student in Turkey.")

student_info = ["Shaimaa", "Future Data Engineer"]

def evaluate_scholarship(grade, language_skill):
    if grade >= 85 and language_skill == "Python":
        return "Strong Candidate for Turkey Scholarship"
    else:
        return "Building more skills for the future"

my_grade = 90
my_skill = "Python"

final_result = evaluate_scholarship(my_grade, my_skill)

print("Student Profile: " + student_info[0] + " - " + student_info[1])
print("Evaluation Result: " + final_result)
print("Project Status: Success on GitHub")
