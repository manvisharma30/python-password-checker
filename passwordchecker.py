
def checker(password):
    has_upper=False
    has_lower=False
    has_number=False
    has_special=False
    special_characters = "@#$%&*+_^?"
    for char in password:
        if char.isupper():
           has_upper=True
        elif char.islower():
               has_lower=True
        elif char.isdigit():
                   has_number=True
        elif char in special_characters:
                   has_special=True
                   
                   
    if len(password) >= 8 and has_upper and has_lower and has_number and has_special:
          print("strong password")
    elif len(password)>=6 and has_upper and has_lower and has_number and has_special:
          print("medium password")
    else:
            print("weak password")
            
            
password = input("Enter your password: ")
checker(password)
