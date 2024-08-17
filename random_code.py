import os
import random

def cleor():
    os.system("clear")
    
cleor()

a = [] 
def kiritish():        
     
    cleor()
    print("Sizning kodingiz:")
    
    for i in range(parol):
        randon = random.choice([random.randint(48, 57), random.randint(97, 122)])
        a.append(randon)
        print(chr(randon), end='')  
while True:         
    parol = int(input("\nKodingiz nechta sondan iborat bo'lsin: "))
    if parol < 8 or parol > 12:
        print("8-dan yuqori 12-dan kichik son kiriting")
        break
    else: 
   
        kiritish()
        
   

