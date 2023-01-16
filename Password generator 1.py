import random

def shuffle(pas):
    temp=list(pas)
    random.shuffle(temp)
    return ''.join(temp)

def main():
    uc1=chr(random.randint(65,90))
    uc2=chr(random.randint(65,90))
    lc1=chr(random.randint(97,122))
    lc2=chr(random.randint(97,122))
    d1=str(random.randint(0,9))
    d2=str(random.randint(0,9))
    ps1=chr(random.randint(33,38))
    ps2=chr(random.randint(33,38))
    pas=uc1+uc2+lc1+lc2+d1+d2+ps1+ps2
    #print(pas)
    password=shuffle(pas)
    print("your auto genrated password is: ",password)

main()

