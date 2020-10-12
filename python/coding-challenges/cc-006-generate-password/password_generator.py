from os import name
import random as rnd
name = "MusaErmeydan"
#name = input("Please enter your full name (without any space): ")
passw = ""
for i in range(3):
  randIndex = rnd.randint(0, len(name)-1)
  letter = name[randIndex]
  passw += letter.lower()
randNum = rnd.randint(1000,9999)
passw += str(randNum)
print(passw)