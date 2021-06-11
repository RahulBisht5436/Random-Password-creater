database = {
    "rdfgjhgfhdgvhv.com": "insuyugjfgdjsh5436",
    "tsdhgfhkuheuwhefjd": "jgjhsdhggjgdgfgjsj",
    "jygyffgidshdfhetugsdhbd": "hgjchsdgjjhgsdjhgf",
    "uayggfcjdkhsieuygbjjkgjgjdg": "ghgdfgdjgsjgdugbjshhd",
    "1234": "1234"
}
     # RANDOM MAIL AND PASSWORD GENERATOR
import random
u=1
student=int(input("how many student are there"))
while u<student+1:
  student_rollno=str(1900950100000+u)
  alnu="1234567890qwertyuiopasdfghjklzxcvbnm"
  
  for x in range(1,student):
    y=0
    password=""
    while y<12:
      password_bit=random.choice(alnu)
      password+=password_bit
      y+=1
    database[student_rollno +".COET"] = [password]
  u+=1   

for x in database.items():
   print(x)
