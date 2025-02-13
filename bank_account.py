import json
import re
from projects.bank.operations_to_json import add_new_account, search_id_in_json, add_balance, remove_money, view_account, view_accounts, transfer,apply_for_a_loan,repay_curr_loan

def check(name):
    with open("example.json", "r") as file:
        data = json.load(file)
    if name in data:
        return True

def name_check(name:str) -> bool: # checks the name and returns True or False
    """Checks name using regex."""
    pattern = r"^([A-Z][a-z]+(?:-[A-Z][a-z]+)?)((\s[A-Z][a-z]+(?:-[A-Z][a-z]+)?)*)$" #checks for hyphens in name
    match = re.fullmatch(pattern, name) #uses regex to check if the name is valid
    return bool(match)


def create_new_account():
    """Create a new bank account."""
    full_name = input("Please write your full name: ") #prompts user to write a valid name
    if name_check(full_name):
        print(f"Valid name! Welcome {full_name}!")
        print(add_new_account(full_name)) # Adds user to the json with a balance of 0, empty transaction history, and no loan
    else:
        print("Invalid name, please try again")


def deposit():
    """Deposit money into an account."""
    user_id = input("Please write your ID: ")
    if search_id_in_json(user_id):
        try:
            amount = float(input("Welcome, please enter amount: "))
            print(add_balance(user_id, amount))
        except ValueError:
            print("Error, please try again")
    else:
        print("Sorry your ID is not valid, please try again.")


def withdraw():
    """Withdraw money from an account."""
    user_id = input("Please write your login ID: ")
    if search_id_in_json(user_id):
        try:
            amount_to_withdraw = float(input("Please enter amount: "))  #prompts user to withdraw a value
            print(remove_money(user_id, amount_to_withdraw))
        except ValueError:
            print("Error, please try again")
    else:
        print("Sorry your name is not valid, please try again.")


def check_balance():
    """Check the balance of an account."""
    user_id = input("Please write your login ID: ")
    if search_id_in_json(user_id):
        print(view_account(user_id))
    else:
        print("Sorry your name is not valid, please try again.")


def list_accounts():
    """List all accounts and their balances."""
    print(view_accounts())

def transfer_funds():
    """Transfer funds between two accounts."""
    user_id = input("Please write your login ID: ")
    recipients_user = input("Who would you like to transfer funds to (ID): ")
    if search_id_in_json(user_id) and search_id_in_json(recipients_user):
        print("Users found")
        try:
            amount_to_transfer = float(input("How much would you like to transfer: "))
            print(transfer(user_id, recipients_user, amount_to_transfer))
        except ValueError:
            print("Error, please try again")
    else:
        print("Sorry names are not valid, please try again.")

def apply_for_loan():
    """Apply for a loan."""
    user_id = input("Please write your login ID: ")
    if search_id_in_json(user_id):
        loan_amount = float(input(f"Enter the loan amount (max 10 000): "))
        print(apply_for_a_loan(user_id, loan_amount))
    else:
        print("Sorry your name is not valid, please try again.")


def repay_loan():
    """Repay a loan."""
    user_id = input("Please write your login ID: ")
    if search_id_in_json(user_id):
        print(repay_curr_loan(user_id))
    else:
        print("Sorry your name is not valid, please try again.")


def display_menu():
    """Display the main menu."""
    print("\n--- Bank Account Management System ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. List Accounts")
    print("6. Transfer Funds")
    print("7. Apply for Loan")
    print("8. Repay Loan")
    print("9. Exit")

    # Prompt user for their choice
    choice = int(input("Enter your choice: "))
    return choice


def main():
    """Main function to run the banking system."""
    while True:
        choice = display_menu()  # Display the menu and get user choice

        # Process user input based on their choice
        if choice == 1:
            create_new_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            apply_for_loan()
        elif choice == 8:
            repay_loan()
        elif choice == 9:
            print("Exiting the system. Goodbye!")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice. Please try again.")

main()
