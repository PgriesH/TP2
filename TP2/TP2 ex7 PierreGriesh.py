import random

nb =random.randint(1, 100)

print(nb)

if nb < 50:
    print ("Pile")
if nb > 50:
    print ("Face")
if nb > 75:
    print("Pile")

