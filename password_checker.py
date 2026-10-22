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
    else
        feedback.append("Your password is too short")