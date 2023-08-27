import random

smallLetters="abcdefghijklmnopqrstuvwxyz"
capitalLetters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
specialCharacters='''!@#$%^&*_-+=:;"'/?><,.'''
password=[]
for i in range(10):
    a = random.randint(1,4)
    if a==1:
        password.append(smallLetters[random.randint(0,len(smallLetters)-1)])
    elif a==2:
        password.append(capitalLetters[random.randint(0,len(capitalLetters)-1)])
    elif a==3:
        password.append(numbers[random.randint(0,len(numbers)-1)])
    else:
        password.append(specialCharacters[random.randint(0,len(specialCharacters)-1)])

print("Password","".join(password))

                