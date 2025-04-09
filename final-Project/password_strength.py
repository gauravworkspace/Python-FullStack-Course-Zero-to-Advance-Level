import re 

# alteast 8 char , digit, uppercase,lowercase,special symbol 
def check_password_strength(password):
    if len(password) < 8:
        return "Weak : Password must be 8 character!."
    if not any(char.isdigit() for char in password):
        return "Weak : Password must contain a digit"
    if not any(char.isupper() for char in password):
        return "Weak : Password must be contain Upper Character"
    if not any(char.islower() for char in password):
        return "Weak : Password must be contain Lower Character"
    if not re.search(r'[!@#$%^&*():;?/><.,|`~]',password):
        return " Medium : Password must contain a special character"
    return "Strong: Your Password is secured!"
    

def check_password():
    print("Welcome to the password strength checker ")
    while True:
        password = input("Enter Your Password (or type 'exit' to quite ): ")

        if password.lower() == 'exit':
            return "Thank you for using this tool"
            break
        result = check_password_strength(password)
        print(result)
        break
    

# Run the password check tool
if __name__ == "__main__":
    check_password()
