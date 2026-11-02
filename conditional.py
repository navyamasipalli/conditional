
print("Welcome to Navya's College Story")

name = input("Enter your name: ")
print("Good morning", name)

time = int(input("Enter your waking time (hour): "))

if time <= 6:
    print("You woke up early")
elif time <= 8:
    print("You woke up on time")
else:
    print("You woke up late")

print("Getting ready for college")

breakfast = input("Did you eat breakfast? yes/no: ")

if breakfast == "yes":
    print("You are energetic")
else:
    print("You are hungry")

bus = input("Did you catch the bus? yes/no: ")

if bus == "yes":
    print("You reached college safely")
else:
    print("You are late to college")

attendance = int(input("Enter attendance percentage: "))

if attendance >= 75:
    print("You are eligible for exams")
else:
    print("Attendance is insufficient")

marks = int(input("Enter exam marks: "))

if marks >= 90:
    print("Excellent performance")
elif marks >= 75:
    print("Very good performance")
elif marks >= 50:
    print("You passed")
else:
    print("You failed")

homework = input("Did you complete homework? yes/no: ")

if homework == "yes":
    print("Enjoy your free time")
else:
    print("Complete your homework")

print("End of Navya's College Story")
