accounts = {
    "admin1": {
        "password": "secure99",
        "role": "admin",
        "is_locked": False,
        "failed_attempts": 0,
        "password_change_count": 1
    },
    "alice": {
        "password": "pass123",
        "role": "student",
        "is_locked": False,
        "failed_attempts": 0,
        "password_change_count": 0
    },
    "mr_tan": {
        "password": "teach88",
        "role": "lecturer",
        "is_locked": False,
        "failed_attempts": 2,
        "password_change_count": 2
    }
}


def is_strong_password(password: str) -> bool:
    if password.isalpha() or password.isnumeric():
        return False
    return True

def create_user(accounts: dict, username: str, password: str, role: str) -> bool:
    
    valid_roles = ["student", "lecturer", "admin"]

    if role.lower() not in valid_roles:
        return False
    
    if username in accounts:
        return False
    
    if len(password) < 6:
        return False
    
    if not is_strong_password(password):
        return False
    
    accounts[username] = {}
    
    accounts[username]['password'] = password
    accounts[username]['role'] = role
    accounts[username]['is_locked'] = False
    accounts[username]['failed_attempts'] = 0
    accounts[username]['password_change_count'] = 0

    return True


def delete_user(accounts: dict, admin_username: str, target_username: str) -> str:
    if admin_username not in accounts or accounts[admin_username]['role'] != "admin":
        return "Permission denied"
    
    if target_username not in accounts:
        return "Target user not found"
    accounts.pop(target_username)
    return "User deleted successfully"


def login(accounts: dict, username: str, password: str) -> str:
    if username not in accounts:
        return "User not found"
    
    if accounts[username]['is_locked'] == True:
        return "Account locked"
    
    if password != accounts[username]['password']:
        
        accounts[username]['failed_attempts'] += 1
        if accounts[username]['failed_attempts'] == 3:
            accounts[username]['is_locked'] = True 
        return "Invalid password"
    else:
        accounts[username]['failed_attempts'] = 0
        return "Login successful"
    
    
def change_password(accounts: dict, username: str, old_password: str, new_password: str) -> str:
    if username not in accounts:
        return "User not found"
    elif accounts[username]['is_locked'] == True:
        return "Account locked"
    elif old_password != accounts[username]['password']:
        return "Old password incorrect"
    elif new_password == old_password or len(new_password) < 6 or not is_strong_password(new_password):
        return "New password invalid"
    else:
        accounts[username]['password'] = new_password
        accounts[username]['password_change_count'] += 1
        return "Password changed successfully"
    
    
def unlock_user(accounts, admin_username, target_username) -> str:
    if admin_username not in accounts or accounts[admin_username]['role'] != "admin":
        return "Permission denied"
    
    if target_username not in accounts:
        return "Target user not found"
    
    if accounts[target_username]['is_locked'] != True:
        return "User is not locked"
    
    accounts[target_username]['is_locked'] = False
    accounts[target_username]['failed_attempts'] = 0
    return "User unlocked successfully"


def get_account_summary(accounts: dict) -> dict:
    total_users = len(accounts)

    to_return = {
        "total_users" : total_users,
        "locked_accounts" : 0,
        "admins": 0,
        "students": 0,
        "lecturers": 0,
        "most_password_changes": None
    }

    password_change_counter = {}

    if total_users == 0:
        return to_return
    
    for account in accounts:
        if accounts[account]['is_locked'] == True:
            to_return["locked_accounts"] += 1
        
        if accounts[account]['role'] == 'admin':
            to_return["admins"] += 1
        elif accounts[account]['role'] == "student":
            to_return["students"] += 1
        elif accounts[account]['role'] == "lecturer":
            to_return["lecturers"] += 1

        if account not in password_change_counter:
            password_change_counter[account] = accounts[account]['password_change_count']

    to_return["most_password_changes"] = max(password_change_counter, key=password_change_counter.get)

    return to_return


def get_role_report(accounts: dict) -> dict:
    to_return = {
        "admins": None,
        "students": None,
        "lecturers": None,
    }

    if len(accounts) == 0:
        return to_return
    else:
        to_return["admins"] = []
        to_return["students"] = []
        to_return["lecturers"] = []
    
    for account in accounts:
        role = accounts[account]['role']
        if role == "admin":
            to_return["admins"].append(account)
        elif role == "student":
            to_return["students"].append(account)
        elif role == "lecturer":
            to_return["lecturers"].append(account)

    return to_return


