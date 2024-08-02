import random
import string
def password():
    #using String library to get letters, special characters, and digits
    letters=string.ascii_letters
    digits= string.digits
    spl_char= string.punctuation

    #combine all the letters, special characters, and digits
    characters= letters + digits + spl_char

    #check the minimum length of password
    while True:
        try:
            l=int(input("Enter the Password Length (min:8) :"))
            
            if l>=8: #to check the length of "l" greater than or equal to 8
                break
        except ValueError: #ValueError helps to handle errors in the input
            print("Enter a valid number :")

    while True:
        pwd=random.choices(characters, k=l)  #random function to select the password randomly
        
        #Boolean Flags
        has_digit=False 
        has_letter=False
        has_splchar=False
        
        for i in pwd:
            if i in digits: #if digits occur in password make False into True
                has_digit=True
            elif i in letters:
                has_letter=True
            elif i in spl_char:
                has_splchar=True
            # if all Flags are true break loop
            if has_digit and has_digit and has_digit:
                break
        #checking the criteria
        if has_digit and has_digit and has_digit:
            break

    #ignore this
    ascii="""
  _____                                    _     
 |  __ \                                  | |    
 | |__) |_ _ ___ _____      _____  _ __ __| |    
 |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` |    
 | |  | (_| \__ \__ \\ V  V / (_) | | | (_| |    
 |________,_|___/___/ \_/\_/ \___/|_|  \__,_|    
  / ____|                         | |            
 | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                 
    """
    print(ascii)
    pwd=''.join(pwd) #joins all the list into pwd without any separators
    print("_"*80) #to print "_" 80 times
    print("Your Password is:", pwd, "you Copy the Password ") #printing the password
    print("_"*80)
password() #calls the function
while True: #runs until the codition is false
    c=input("Want to generate more? [y/n] ").lower() #asks user to continue
    if c=="y":
        password() 
    else:
        print("_"*80)
        print("Thanks for using Password Generator! \n            -Made by Gururagavendra")
        print("_"*80)
        break