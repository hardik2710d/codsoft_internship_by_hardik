import random

characters=['!','@','#','$','%','','&','*','_','-']
numbers=['1','2','3','4','5','6','7','8','9','0']
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cap_letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



def password():
    part1= length//2
    remaining= length-part1
    a,b= sorted(random.sample(range(1,remaining),2))
    
    letters_n= part1
    characters_n= a
    numbers_n= b-a
    cap_letters_n= remaining-b

    password=[]
    
    for i in range(1,letters_n+1):
        a=random.choice(letters)
        password+=a
        
    for i in range(1,characters_n+1):
        a=random.choice(characters)
        password+=a

    for i in range(1,numbers_n+1):
        a=random.choice(numbers)
        password+=a
        
    for i in range(1,cap_letters_n+1):
        a=random.choice(cap_letters)
        password+=a
        
    password1=""
    for i in password:
        password1+=i

    print("password is: ",password1)


def strong_password():
    part1= length//3
    remaining= length-part1
    a,b= sorted(random.sample(range(1,remaining),2))
    
    letters_n= part1
    characters_n= a
    numbers_n= b-a
    cap_letters_n= remaining-b

    password=[]
    
    for i in range(1,letters_n+1):
        a=random.choice(letters)
        password+=a
        
    for i in range(1,characters_n+1):
        a=random.choice(characters)
        password+=a

    for i in range(1,numbers_n+1):
        a=random.choice(numbers)
        password+=a
        
    for i in range(1,cap_letters_n+1):
        a=random.choice(cap_letters)
        password+=a
        
    random.shuffle(password)
    
    password1=""
    
    for i in password:
        password1+=i

    print("password is: ",password1)

def strongest_password():
    part1= length//4
    remaining= length-part1
    a,b= sorted(random.sample(range(1,remaining),2))
    
    letters_n= part1
    characters_n= a
    numbers_n= b-a
    cap_letters_n= remaining-b

    password=[]
    
    for i in range(1,characters_n+1):
        a=random.choice(letters)
        password+=a
        
    for i in range(1,letters_n+1):
        a=random.choice(characters)
        password+=a

    for i in range(1,numbers_n+1):
        a=random.choice(numbers)
        password+=a
        
    for i in range(1,cap_letters_n+1):
        a=random.choice(cap_letters)
        password+=a
        
    random.shuffle(password)
    
    password1=""
    for i in password:
        password1 += i

    print("password is: ", password1)
   

    
    
length=int(input("enter the length of the password: "))
user=int(input("enter the complexity level of password(1/2/3): "))



while True:
    if length>5:
        if user==1:
            password()
            a=input("enter yes(y) if you want another password if not then no(n): ")
            if a=="y":
                continue
            else:
                break
    
        elif user==2:
            strong_password()
            a=input("enter yes(y) if you want another password if not then no(n): ")
            if a=="y":
                continue
            else:
                break
            
    

        elif user==3:
            strongest_password()
            a=input("enter yes(y) if you want another password if not then no(n): ")
            if a=="y":
                continue
            else:
                break

        else:
            print("invalid input")
            a=input("enter yes(y) if you want another try if not then no(n): ")
            if a=="y":
                continue
            else:
                break

    else:
        print("lenght should be more than 5 for a password")
        break

