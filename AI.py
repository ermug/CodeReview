import os
import google.generativeai as genai

# Send our API Key to google for authentication
GOOGLE_API_KEY = "AIzaSyDcx80pzVdDVBFrjDWqRord4Ru7aArAA84"
genai.configure(api_key=GOOGLE_API_KEY)

# Creates a chat using a gemini model
model = genai.GenerativeModel('gemini-2.0-flash-thinking-exp-01-21')
chat = model.start_chat(history=[])


# Function to read the code from a file
def read_code_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            code = file.read()
        return code
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

# Debugging Assistance
def debugging_assistance(file_path):
    print("Mode: Debugging Assistance")
    code_to_debug = read_code_from_file(file_path)  # Read the code from the file
    if code_to_debug:
        # Ask the AI to provide a debugging overview
        prompt = f"Provide an overview of issues with this code:\n{code_to_debug}\n"
        response = chat.send_message(prompt, stream=True)
        # Print the response from the AI
        for chunk in response:
            if chunk.text:
                print(chunk.text)


# Code Consistency Checker
def consistency_checker(file_path):
    print("Mode: Code Consistency Checker")
    code_to_check = read_code_from_file(file_path)  # Read the code from the file
    if code_to_check:
        # Ask the AI to check for code consistency
        prompt = f"Check the following code for consistency and highlight any potential issues:\n{code_to_check}\n"
        response = chat.send_message(prompt, stream=True)
        # Print the response from the AI
        for chunk in response:
            if chunk.text:
                print(chunk.text)


# Refactoring Code
def refactor_code(file_path):
    print("Mode: Refactoring Code")
    code_to_refactor = read_code_from_file(file_path)  # Read the code from the file
    if code_to_refactor:
        # Ask the AI to refactor the code for consistency
        prompt = f"Refactor the following code to make it consistent, clean, and efficient:\n{code_to_refactor}\n"
        response = chat.send_message(prompt, stream=True)
        # Print the refactored code from the AI
        for chunk in response:
            if chunk.text:
                print(chunk.text)


# Free Mode (Free Conversation)
def free_mode():
    print("Mode: Free Mode - You can chat freely with the AI.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            main_menu()
        prompt = f"User: {user_input}\nAI:"
        response = chat.send_message(prompt, stream=True)
        for chunk in response:
            if chunk.text:
                print(f"AI: {chunk.text}")


# Main menu for feature selection
def main_menu():
    print("\nChoose a mode:")
    print("1.) Debugging Assistance")
    print("2.) Code Consistency Overview")
    print("3.) Refactoring Code")
    print("4.) Free Mode")
    print("5.) Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        file_path = input("Please enter the file path of your code: ").strip()  # Get file path from the user
        if file_path.lower() == "exit":
            main_menu()
        debugging_assistance(file_path)
        print()
        input("Press anything to return to main menu: ")
        main_menu()

    elif choice == 2:
        file_path = input("Please enter the file path of your code: ").strip()  # Get file path from the user
        if file_path.lower() == "exit":
            main_menu()
        consistency_checker(file_path)
        print()
        input("Press anything to return to main menu: ")
        main_menu()

    elif choice == 3:
        file_path = input("Please enter the path to the code file you want to refactor: ").strip()  # Get file path from the user
        if file_path.lower() == "exit":
            main_menu()
        refactor_code(file_path)
        print()
        input("Press anything to return to main menu: ")
        main_menu()

    elif choice == 4:
        free_mode()

    elif choice == 5:
        exit()

    else:
        print("Invalid choice! Please try again.")
        main_menu()


if __name__ == "__main__":
    main_menu()
