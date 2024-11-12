import os

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

    # Function to print text in different colors
def print_colored(text, color_code, end='\n'):
    print(f"\033[{color_code}m{text}\033[0m", end=end)


clear_screen()  # Clear the screen before starting the quiz
print_colored(" Welcome to the Pub Quiz! ", "1;30;47")  # Welcome message for the quiz

# List of questions, options, and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
        "prompt": "Your answer (A, B, C, D): ",
        "answer": "B"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 22"],
        "prompt": "Your answer (A, B, C, D): ",
        "answer": "B"
    },
    {
        "question": "What is the airspeed of an unladen swallow?",
        "options": ["A) 33 mph", "B) 25 mph", "C)  40 mph", "D) 45 mph"],
        "prompt": "Your answer (A, B, C, D): ",
        "answer": "C"
    },
    {
        "question": "What is Batmans real name?",
        "options": ["A) Clark Kent", "B) Bruce Wayne", "C)  Dick Grayson", "D) Diana Prince"],
        "prompt": "Your answer (A, B, C, D): ",
        "answer": "B"
    },
    {
        "question": "What is your name?",
        "options": ["Please enter your name"],
        "prompt": "Fullname: ",
        "answer": "name"
    },
    # Learners can add more questions here following the same structure
]

# Variable to store the user's score
score = 0
name = ""

# Loop through each question
for question in quiz_questions:
    # Display the question and options
    print(question["question"])
    for option in question["options"]:
        #print(option)
        print_colored(option.split()[0], "1;37", end=' ')
        print(option.split()[1])
            
    # Check if the question is asking for the user's name
    if question["question"] == "What is your name?":
        name = input(question["prompt"]).capitalize()
        score += 1 # Increment the score if the answer is correct
        clear_screen() # Clear the screen for the next question
        continue # Skip the rest of the loop    

    # Get the user's answer
    user_answer = input(question["prompt"]).strip().upper() # Ensuring the input is uppercase for comparison

    # Check if the answer is correct
    if user_answer == question["answer"]:
        print_colored("Correct!", "1;32") 
        score += 1 # Increment the score if the answer is correct
    else:
        print_colored(f"Wrong! The correct answer was {question['answer']}.", "1;31") 
        #print(f"Wrong! The correct answer was {question['answer']}.")

    input("Continue...")  # Pause the program until the user presses Enter
    clear_screen() # Clear the screen for the next question


# Goodbye message
print(f"Thank you {name} for playing the Pub Quiz!")
print(f"You scored {score} out of {len(quiz_questions)}")
