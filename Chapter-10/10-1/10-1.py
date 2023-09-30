import re
def main():
    full_name = get_full_name()
    print()
    email = get_email()
    print()
    phone = get_phone()
    print()
    password = get_password()
    print()
    
    first_name = get_first_name(full_name)   
    print(f"Hi {first_name}, thanks for creating an account.")  
    print(f"We will text your confirmation code to {phone}") 
    
def get_full_name():
    while True:
        name = input("Enter full name:       ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")
    
def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name

#ok so the book does these different then how i do it here. i guess the advantage of that is you dont need to import but i find this way easier and more customizable


def get_email():
 isvalid = 0
 while isvalid == 0 :
    email = input("enter your email:   ").strip()
    pattern = re.compile(r"[A-Za-z]+@[A-Za-z0-9]+\.[A-Za-z0-9]+", re.IGNORECASE)
    if re.match(pattern, email) :
        return email
    else :
        print("please enter a valid email")

def get_phone():
   while True :
    phone = input("what is your phone number:  ")
    pattern = re.compile(r"\d\d\d[.\-\040]\d\d\d[.\-\040]\d\d\d\d", re.IGNORECASE)
    if re.match(pattern,phone) :
        return phone
    else: print("phone number invalid")



def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:        ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print(f"Password must be 8 characters or more \n"
                  f"with at least one digit and one uppercase letter.")
        else:
            return password
        
if __name__ == "__main__":
    main()
