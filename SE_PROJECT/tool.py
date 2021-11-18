import string

def checkLength(length):
    if not length:
        print("Length cannot be null")
        return False
    elif length.isalpha():
        print("Length should be a number")
        return False
    elif not int(length):
        print("Length should be non-zero")
        return False
    elif int(length) < 0:
        print("Length should not be neagtive")
        return False
    else:
        return True

def validatePassword(length, options, password):
    feedback = []
    if(int(length) != len(password)):
        feedback.append("The password length and the length specified do not match")
    elif not options:
        feedback.append("No options are selected")
    else:
        for option in options:
            if option == "uppercase":
                if not passwordContains(password,string.ascii_uppercase):
                    feedback.append("Password does not contain an uppercase letter")
            elif option == "lowercase":
                if not passwordContains(password,string.ascii_lowercase):
                    feedback.append("Password does not contain a lowercase letter")
            elif option == "digit":
                if not passwordContains(password,string.digits):
                    feedback.append("Password does not contain a digit")
            elif option == "special":
                if not passwordContains(password,string.punctuation):
                    feedback.append("Password does not contain a special character")
            else:
                print("Invalid option.")
    return feedback


def passwordContains(password, list):
    contains = False
    i = 0
    while(not contains and i < len(password)):
        if password[i] in list:
            contains = True
        i += 1
    return contains

def setFeedback(feedback):
    if not feedback:
        print("Password is valid!")
    else:
        print("Password is invalid:")
        for fb in feedback:
            print(fb)
