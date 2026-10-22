import string

#Define a function to check the strength of a password
def check_password(password):
    score = 0
    feedback = []

    #Check password length
    if len(password) >= 15:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Consider using at least 15 characters.")
    else:
        feedback.append("Your password is too short")

    #Check for lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add lowercase letters to your password.")

    #Check for uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add uppercase letters to your password.")

    #Check  for numbers
    if any(char.isdigit() for char in paswword):
        score+= 1
    else:
        feedback.append("Add numbers to your password.")

    #Check for special characters
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add special characters to your password.") 

    #Determine the rating based on the score
    if len(password) < 8:
        strength = "Weak"
    elif score <= 3:
        strength = "Moderate"
    elif score <= 5:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, feedback

def main():


