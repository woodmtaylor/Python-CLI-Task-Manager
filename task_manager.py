#!/usr/bin/env python3

"""
Python CLI Task Manager
A simple command-line task management application.
"""

def main():
    """Main application that accepts user input."""
    print("Welcome to the Task Manager CLI!")
    print("(Type 'exit' to quit the program)")
    
    while True:
        # Get user input
        user_input = input("\nEnter a command: ")
        
        # Check if user wants to exit
        if user_input.lower() == 'exit':
            print("Thank you for using the Task Manager. Goodbye!")
            break
           
        # Echo the input back to the user (just to show that it's working)
        print(f"You entered: {user_input}")
        print("Command received. Future versions will implement this functionality.")

if __name__ == "__main__":
    main()