import time

students = []
attempts = {}

questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D"
    },
    {
        "question": "What is the output type of input() function?",
        "options": ["A. int", "B. float", "C. str", "D. bool"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. /* */", "D. --"],
        "answer": "B"
    },
    {
        "question": "Which function displays output on screen?",
        "options": ["A. show()", "B. display()", "C. print()", "D. output()"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used for looping?",
        "options": ["A. repeat", "B. for", "C. iterate", "D. loop"],
        "answer": "B"
    },
    {
        "question": "Which collection stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. String"],
        "answer": "C"
    },
    {
        "question": "Which operator is used for exponentiation?",
        "options": ["A. ^", "B. **", "C. //", "D. %"],
        "answer": "B"
    },
    {
        "question": "What is the extension of a Python file?",
        "options": ["A. .java", "B. .cpp", "C. .py", "D. .html"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used for conditional statements?",
        "options": ["A. case", "B. switch", "C. if", "D. choose"],
        "answer": "C"
    }
]

while True:

    print("\n====== SMART QUIZ AND EXAMINATION SYSTEM ======")

    print("1. Student Login")
    print("2. Teacher Dashboard")
    print("3. Exit")

    choice = input("\nEnter Choice : ")

    if choice == "1":

        name = input("\nEnter Student Name : ")
        roll = input("Enter Roll Number  : ")

        # Attempt Checking
        if roll in attempts:
            if attempts[roll] >= 2:
                print("\nAttempt Limit Exceeded!")
                print("You have already used 2 out of 2 attempts.")
                print("Quiz Access Denied.")
                continue
        else:
            attempts[roll] = 0

        attempts[roll] += 1

        print(f"\nAttempts Used : {attempts[roll]} / 2")

        score = 0
        correct = 0
        total_time = 0

        print("\n========== QUIZ STARTED ==========")

        for i, q in enumerate(questions, start=1):

            print(f"\nQ{i}. {q['question']}")

            for option in q["options"]:
                print(option)

            start_time = time.time()

            answer = input("Your Answer : ").upper()

            end_time = time.time()

            solved_time = round(end_time - start_time, 2)
            total_time += solved_time

            print("Solved In :", solved_time, "sec")

            if answer == q["answer"]:
                print("Correct Answer")
                score += 1
                correct += 1
            else:
                print("Wrong Answer")

        wrong = len(questions) - correct

        percentage = (score / 10) * 100

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B+"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "F"

        result = "PASS" if percentage >= 40 else "FAIL"

        students.append({
            "name": name,
            "roll": roll,
            "attempt": attempts[roll],
            "score": score,
            "percentage": percentage,
            "grade": grade,
            "result": result,
            "time": round(total_time, 2)
        })

        print("\n====== QUIZ RESULT ======")

        print("Student Name    :", name)
        print("Roll Number     :", roll)
        print("Attempt No      :", attempts[roll])
        print("Correct Answers :", correct)
        print("Wrong Answers   :", wrong)
        print("Score           :", score, "/10")
        print("Percentage      :", round(percentage, 2), "%")
        print("Grade           :", grade)
        print("Result          :", result)
        print("Total Time      :", round(total_time, 2), "sec")

    elif choice == "2":

        if len(students) == 0:
            print("\nNo Student Records Found!")
            continue

        print("\n====== STUDENT PERFORMANCE REPORT =======")

        print("NO\tROLL\tNAME\tATT\tSCR\t%\tGRADE\tRESULT\tTIME")

        for i, s in enumerate(students, start=1):

            print(
                f"{i}\t{s['roll']}\t{s['name']}\t{s['attempt']}\t"
                f"{s['score']}\t{round(s['percentage'])}\t"
                f"{s['grade']}\t{s['result']}\t{s['time']}"
            )

        print("\nTotal Students :", len(students))

        topper = max(students, key=lambda x: x["score"])

        print("\n================ TOP PERFORMER ================")
        print("Name       :", topper["name"])
        print("Roll No    :", topper["roll"])
        print("Score      :", topper["score"], "/10")
        print("Percentage :", round(topper["percentage"], 2), "%")
        print("Grade      :", topper["grade"])
        print("Result     :", topper["result"])

    elif choice == "3":

        print("\nThank You For Using Smart Quiz System!")
        break

    else:
        print("\nInvalid Choice! Please Try Again.")