# importing time, so we can detect how long takes cracking
import os
import time

def initialize_file():
    '''Checks if file does exist, if not, it creates one '''
    if (os.path.exists("log.txt") == False):
        f = open("log.txt", 'a')
        f.close()

def append_file(text):
    '''
    Adds text to txt document
    :param str text
    '''
    f = open("log.txt", 'a')
    f.write(text)
    f.close()

def is_valid_password(password):
    '''
    Checks if there are 8 characters in password
    :param str password: the password that will be cracked
    '''
    return len(password) == 8

def password_strength(password):
    '''
    Determines the strength of the cracked password
    :param str password: the password that will be cracked
    '''
    
    length_criteria = 8
    uppercase_criteria = lowercase_criteria = digit_criteria = special_char_criteria = False

    for char in password:
        if char.isupper():
            uppercase_criteria = True
        elif char.islower():
            lowercase_criteria = True
        elif char.isdigit():
            digit_criteria = True
        elif char in "!@#$%^&*()_-+=<>?/":
            special_char_criteria = True

    if (
        len(password) >= length_criteria
        and uppercase_criteria
        and lowercase_criteria
        and digit_criteria
        and special_char_criteria
    ):
        return "Strong"
    elif (
        len(password) >= length_criteria
        and (
            (uppercase_criteria and lowercase_criteria)
            or (uppercase_criteria and digit_criteria)
            or (lowercase_criteria and digit_criteria)
        )
    ):
        return "Medium"
    else:
        return "Weak"

def crack_password(root, cracked_password_label, password):
    '''Brute-Force password cracking process happens here
    :param root: TKinter window
    :param str cracked_password_label:all the labels appearing in the window
    :param str password: the password that will be cracked
    '''
    append_file(f"Trying to crack {password}:\n")

    if not is_valid_password(password):
        cracked_password_label.configure(text="Password must be 8 characters long. Please retry.")
        return

    strength = password_strength(password)

    characters = ""
    for i in range(97, 123):
        characters += chr(i)
    for i in range(48, 58):
        characters += chr(i)
    for i in range(65, 91):
        characters += chr(i)

    characters += chr(95) + chr(45) + chr(33) + chr(35) + chr(36) + chr(64) + chr(32)


    cracked_password = None
    attempt_count = 0

    start_time = time.time()

    for char1 in characters:
        for char2 in characters:                     
            for char3 in characters: 
                for char4 in characters:                                                                                        
                    for char5 in characters:
                        for char6 in characters:
                            for char7 in characters:
                                for char8 in characters:
                                    attempt_count += 1
                                    attempt = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8
                                    cracked_password_label.configure(text=f"Attempt {attempt_count}: {attempt}")
                                    root.update_idletasks()
                                    if attempt == password:
                                        cracked_password = attempt
                                        break
                                if cracked_password:
                                    break
                            if cracked_password:
                                break
                        if cracked_password:
                            break
                    if cracked_password:
                        break
                if cracked_password:
                    break
            if cracked_password:
                break
        if cracked_password:
            break

    end_time = time.time()
    time_spent = end_time - start_time
    append_report = f"Cracked Password: {cracked_password}\nAttempts: {attempt_count}\nTime Spent: {time_spent:.2f} seconds\nPassword Strength: {strength}"

    cracked_password_label.configure(
        text=append_report,
        wraplength=200
    )
    append_file(f"{append_report} \n\n")