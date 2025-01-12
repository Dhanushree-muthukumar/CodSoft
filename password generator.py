import string
import random
def password_generate():
    print("welcome to the password generator")
    
    try:
        a = int(input("Enter password a (min 10): "))
        if a < 10:
            print("password must be at least 10 characters.")
            return
        
        b = input("Include symbols? (yes/no): ").strip().lower()
        chars = string.ascii_letters + string.digits
        if b == "yes":
             chars += string.punctuation
             
        password = ''.join(random.choices(chars, k=a))
        print(f"your genetrated password: {password}")

    except:
        print("incorrect input. length must be numeric value.")
        
password_generate()
        
