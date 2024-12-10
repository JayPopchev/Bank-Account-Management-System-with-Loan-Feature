import re
information_dictionary = {}


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
        information_dictionary[full_name] = {"Balance": 0, "Transaction_history" : ['Account created.'], "Loan": 0} # creates user account
    else:
        print("Invalid name, please try again")


def deposit():
    """Deposit money into an account."""
    full_name = input("Please write your login name: ")
    if full_name in information_dictionary:
        amount_to_deposit = float(input("Please enter amount: ")) #prompts user to deposit a value
        information_dictionary[full_name]["Balance"] += amount_to_deposit #adds the deposit to balance
        information_dictionary[full_name]["Transaction_history"].append(f"Deposited {amount_to_deposit}") #add new data to history
        print(f"Successful deposit of {amount_to_deposit}")
    else:
        print("Sorry your name is not valid, please try again.")


def withdraw():
    """Withdraw money from an account."""
    full_name = input("Please write your login name: ")
    if full_name in information_dictionary:
        amount_to_withdraw = float(input("Please enter amount: "))  #prompts user to withdraw a value
        if amount_to_withdraw <= information_dictionary[full_name]["Balance"]: #checks if users balance is sufficient
            information_dictionary[full_name]["Balance"] -= amount_to_withdraw
            information_dictionary[full_name]["Transaction_history"].append(f"Withdrawn {amount_to_withdraw}")  # add new data to history
            print(f"Successful withdraw of {amount_to_withdraw}, {information_dictionary[full_name]['Balance']} left")
        else:
            print("Not enough funds.")
    else:
        print("Sorry your name is not valid, please try again.")


def check_balance():
    """Check the balance of an account."""
    full_name = input("Please write your login name: ")
    if full_name in information_dictionary:
        print(f"This is your current balance: {information_dictionary[full_name]['Balance']}")
        information_dictionary[full_name]["Transaction_history"].append(f"User checked balance.")
    else:
        print("Sorry your name is not valid, please try again.")


def list_accounts():
    """List all accounts and their balances."""
    if len(information_dictionary) > 0:
        for name, data in information_dictionary.items():
            print(f"{name} has {data['Balance']} balance and {data['Loan']} loan")
    else:
        print("No users.")


def transfer_funds():
    """Transfer funds between two accounts."""
    full_name = input("Please write your login name: ")
    recipients_user = input("Who would you like to transfer funds to: ")
    if full_name in information_dictionary.keys() and recipients_user in information_dictionary.keys():
        print("Users found")
        amount_to_transfer = float(input("How much would you like to transfer: "))
        if amount_to_transfer <= information_dictionary[full_name]["Balance"]:
            information_dictionary[full_name]["Balance"] -= amount_to_transfer
            information_dictionary[recipients_user]["Balance"] += amount_to_transfer
            information_dictionary[full_name]["Transaction_history"].append(f"User transferred {amount_to_transfer} to {recipients_user}")
            information_dictionary[recipients_user]["Transaction_history"].append(f"User got transferred {amount_to_transfer} from {full_name}")
            print(f"Successful transfer of {amount_to_transfer} to {recipients_user}")
        else:
            print("Not enough funds.")
    else:
        print("Sorry names are not valid, please try again.")

def view_transaction_history():
    """View transaction history for a specific account."""
    full_name = input("Please write your login name: ")
    if full_name in information_dictionary:
        if len(information_dictionary[full_name]['Transaction_history']) > 1:
            print(f"Your transaction history is: {information_dictionary[full_name]['Transaction_history']}")
        else:
            print("There is no transaction history")


def apply_for_loan():
    """Apply for a loan."""
    full_name = input("Please write your login name: ")
    if full_name in information_dictionary:
        loan_amount = float(input(f"Enter the loan amount (max 10 000): "))
        if loan_amount <= 10000:
            information_dictionary[full_name]["Balance"] += loan_amount
            information_dictionary[full_name]["Loan"] += loan_amount * (1 + 0.03)  # Calculate total loan with interest
            print(f"Loan of {loan_amount} approved for {full_name}. New balance: {information_dictionary[full_name]['Balance']}.")
        else:
            print(f"Loan amount exceeds maximum limit of 10 000.")
    else:
        print("Sorry your name is not valid, please try again.")


def repay_loan():
    """Repay a loan."""
    full_name = input("Please write your login name: ")
    if full_name in information_dictionary:
        repayment_amount = float(input(f"Enter repayment amount (Outstanding loan: {information_dictionary[full_name]["Loan"]}): "))
        # Check if the repayment amount is valid
        if repayment_amount <= information_dictionary[full_name]["Loan"]:
            # Update balance and outstanding loan amount
            information_dictionary[full_name]["Balance"] -= repayment_amount
            information_dictionary[full_name]["Loan"] -= repayment_amount
            print(f"Repayment of {repayment_amount} accepted for {full_name}. Remaining loan: {information_dictionary[full_name]['Loan']}.")
        else:
            print("Repayment amount exceeds outstanding loan.")
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
    print("7. View Transaction History")
    print("8. Apply for Loan")
    print("9. Repay Loan")
    print("10. Exit")

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
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            print("Exiting the system. Goodbye!")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice. Please try again.")

main()
