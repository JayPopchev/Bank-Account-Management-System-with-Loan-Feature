import json
import datetime

def search_id_in_json(curr_user_id:str) -> bool:
    with open('accounts_info.json', "r") as file:
        data = json.load(file)

    if curr_user_id in data:
        return True
    return False

def add_new_account(name: str):
    with open('accounts_info.json', "r") as file:
        data = json.load(file)
    user_id = f"{len(data) + 1:04d}"
    data[f'{user_id}'] = {
        "Name": name,
        "Balance": 0,
        "Transaction_history": [f'Account created on {datetime.date.today()}'],
        "Loan": 0,
        "ID": f'{len(data) + 1:04d}'}
    with open('accounts_info.json', "w") as file:
        json.dump(data, file, indent=4)
    return f"Account created! User {name} with ID - {user_id}"

def add_balance(curr_user_id:str, amount:float):
    with open('accounts_info.json', 'r') as file:
        data = json.load(file)

    data[curr_user_id]["Balance"] += amount
    data[curr_user_id]["Transaction_history"].append(f'{amount} deposited on {datetime.date.today()}')
    with open('accounts_info.json', 'w') as file:
        json.dump(data, file, indent=4)
    return f'The sum of {amount:.2f} was added to your account with name - {data[curr_user_id]['Name']}'

def remove_money(curr_user_id:str, amount:float):
    with open('accounts_info.json', 'r') as file:
        data = json.load(file)
    if amount <= data[curr_user_id]['Balance']:
        data[curr_user_id]["Balance"] -= amount
        data[curr_user_id]["Transaction_history"].append(f'{amount} withdrawn on {datetime.date.today()}')
    else:
        return f'The sum is bigger than the balance. Your balance - {data[curr_user_id]['Balance']}'

    with open('accounts_info.json', 'w') as file:
        json.dump(data, file, indent=4)
    return f'The sum of {amount} was withdrawn from your account with name - {data[curr_user_id]['Name']}'

def view_account(curr_user_id:str):
    with open('accounts_info.json', 'r') as file:
        data = json.load(file)
    result = []
    for key, value in data[curr_user_id].items():
        if isinstance(value, list):  # Format lists properly
            value = "\n  - " + "\n  - ".join(value)
        result.append(f"{key}: {value}")

    return "\n".join(result)


def view_accounts():
    with open('accounts_info.json', 'r') as file:
        data = json.load(file)
    if len(data) > 0:
        result = []
        for account_id, account_info in data.items():
            result.append(f"Account ID: {account_info['ID']}")
            result.append(f"Name: {account_info['Name']}")
            result.append(f"Balance: ${account_info['Balance']}")
            result.append("Transaction History:")
            for transaction in account_info['Transaction_history']:
                result.append(f"  - {transaction}")
            result.append(f"Loan: ${account_info['Loan']}")
            result.append("=" * 40)
        return "\n".join(result)
    return "No accounts"

def transfer(curr_user_id_one: str,curr_user_id_two: str, amount: float):
    with open('accounts_info.json', 'r') as file:
        data = json.load(file)

    if data[curr_user_id_one]["Balance"] >= amount:
        data[curr_user_id_one]["Transaction_history"].append(f"{amount} transferred to {data[curr_user_id_two]['Name']}")
        data[curr_user_id_two]["Transaction_history"].append(f"{amount} received from {data[curr_user_id_one]['Name']}")
        data[curr_user_id_one]["Balance"] -= amount
        data[curr_user_id_two]["Balance"] += amount
        with open('accounts_info.json', 'w') as file:
            json.dump(data, file, indent=4)
        return f"{data[curr_user_id_one]['Name']} successfully transferred {amount} to {data[curr_user_id_two]['Name']}."
    return f"Error!"

def apply_for_a_loan(user_id:str, amount:float):
    with open('accounts_info.json', 'r') as file:
        data = json.load(file)
    if amount <= 10000:
        data[user_id]["Balance"] += amount # add the loan to the deposit
        data[user_id]["Loan"] += amount * (1 + 0.03) # Calculate total loan with interest
        data[user_id]["Transaction_history"].append(f"The sum of {amount} was deposited from a loan on {datetime.date.today()}")
        with open('accounts_info.json', 'w') as file:
            json.dump(data, file, indent=4)
        return f"The sum of {amount} was successfully deposited to {data[user_id]['Name']}'s account"
    return "Error!"

def repay_curr_loan(user_id:str):
    with open('accounts_info.json', 'r') as file:
        data = json.load(file)
    repayment_amount = float(input(f"Enter repayment amount (Outstanding loan: {data[user_id]["Loan"]}): "))
    if repayment_amount <= data[user_id]["Loan"] and repayment_amount <= data[user_id]["Balance"]:
        data[user_id]["Balance"] -= repayment_amount
        data[user_id]["Loan"] -= repayment_amount
        with open('accounts_info.json', 'w') as file:
            json.dump(data, file, indent=4)
        return f"Repayment of {repayment_amount} accepted for {data[user_id]['Name']}. Remaining loan: {data[user_id]['Loan']}."
    return "Error!"