import random
# Define the level winnings
level_winnings = [1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

# Customize quiz material
question_bank = [
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "correct_answer": "Jupiter",
    },
    {
        "question": "Which celestial body is at the center of our solar system?",
        "options": ["The Moon", "Pluto", "The Sun", "Mars"],
        "correct_answer": "The Sun",
    },
    {
        "question": "What is the smallest unit of matter?",
        "options": ["Molecule", "Atom", "Proton", "Electron"],
        "correct_answer": "Atom",
    },
    {
        "question": "What is the theory that describes the origin of the universe?",
        "options": ["Big Bang Theory", "Steady-State Theory", "String Theory", "Quantum Theory"],
        "correct_answer": "Big Bang Theory",
    },
    {
        "question": "Who is known for their theory of relativity?",
        "options": ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Stephen Hawking"],
        "correct_answer": "Albert Einstein",
    },
    {
        "question": "Which particle is responsible for carrying the electromagnetic force?",
        "options": ["Neutron", "Proton", "Photon", "Quark"],
        "correct_answer": "Photon",
    },
]

# Greetings
def welcome():
    print("Welcome to Kaun Banega Crorepati: Space and Quantum Edition!")
    player_name = input("Please enter your name: ")
    print(f"Hello, {player_name}! Let's begin the quiz.")

# Display a question
def display_question(question_data):
    print(question_data["question"])
    for i in range(len(question_data["options"])):
        option = question_data["options"][i]
        print(f"{i + 1}. {option}")

# Lifeline: 50-50
def lifeline_50_50(question_data):
    print(question_data["question"])
    option1 = question_data["correct_answer"]
    options = question_data["options"][:]
    options.remove(option1)
    random.shuffle(options)
    print(f"1. {option1}")
    print(f"2. {options[0]}")

# Lifeline: Ask the Audience
def lifeline_ask(question_data):
    print(question_data["question"])
    option1 = question_data["correct_answer"]
    print(f"99% of the audience believes the answer is {option1}")

# Main game function
def game():
    welcome()
    total_winnings = level = 0
    random.shuffle(question_bank)

    for question_data in question_bank:
        display_question(question_data)
        user_choice = int(input("Enter your choice (1-4), Enter 5 For 50-50 Lifeline, 6 For Ask the Audience: "))

        if user_choice < 1 or user_choice > 6:
            print("Invalid choice. Please enter a valid choice.")
            continue

        if user_choice == 5:
            lifeline_50_50(question_data)
            user_choice = int(input("Enter your choice (1 or 2): "))
            if user_choice == 1:
                selected_option = question_data["correct_answer"]
            else:
                selected_option = question_data["options"][1]
        elif user_choice == 6:
            lifeline_ask(question_data)
            user_choice = input("Write your answer: ")
            selected_option = user_choice
        else:
            selected_option = question_data["options"][user_choice - 1]

        if selected_option == question_data["correct_answer"]:
            total_winnings = level_winnings[level]
            print("Correct answer! You won", total_winnings, "points.\n")
            level += 1
        else:
            print("Sorry, that's incorrect. The correct answer was:", question_data["correct_answer"], "\n")
            break

    print("Congratulations! You won a total of", total_winnings, "points.")
    print("Thank you for playing!")

if __name__ == "__main__":
    game()