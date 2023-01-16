import string
import random
ch=list(string.ascii_letters+string.digits+"!@#$%^&*()")

def Gen_pass():
    leng=int(input("Length of password: "))
    random.shuffle(ch)
    password=[]
    for x in range(leng):
        password.append(random.choice(ch))
    random.shuffle(password)
    password="".join(password)
    print(password)

Gen_pass()