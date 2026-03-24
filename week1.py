import random

def run_quiz():
    # 1. this is the list of questions
    questions = [
        {
            "question": "What is the result of 2 ** 3?",
            "options": ["A) 6", "B) 8", "C) 5", "D) 9"],
            "answer": "B"
        },
        {
            "question": "Which keyword is used to create a function?",
            "options": ["A) func", "B) define", "C) def", "D) function"],
            "answer": "C"
        },
        {
            "question": "What function is used to get user input?",
            "options": ["A) get()", "B) input()", "C) read()", "D) listen()"],
            "answer": "B"
        }
    ]

    # 2. Shuffling of the questions
    random.shuffle(questions)

    score = 0
    print("--- Welcome to the Python CLI Quiz! ---")

    # 3. Loop through each question
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        # 4. Handle input and errors
        while True:
            user_choice = input("Your answer (A, B, C, or D): ").strip().upper()
            
            if user_choice in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid input! Please enter only A, B, C, or D.")

        # 5. Check the answer
        if user_choice == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.")

    # 6. Final Results and Feedback
    print("\n" + "="*20)
    print(f"QUIZ OVER! Your Score: {score}/{len(questions)}")
    
    if score == len(questions):
        print("Excellent!")
    elif score >= len(questions) // 2:
        print("Good effort!")
    else:
        print("Try again!")

if __name__ == "__main__":
    run_quiz()