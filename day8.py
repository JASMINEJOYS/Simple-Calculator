import random
random_number=random.randint(1,1000)
count=0

while True:
    num=int(input("Enter your number:"))
    if num==random_number:
        print("Naama Jeichittom!!💃🎉")
        break
    elif num<random_number and num>0:
        print(f"Sorryy😥!! The number is greater than {num}")
    elif num>random_number and num<1000:
        print(f"Noooo😒!! The number is lesser than {num}")
    else:
        print("The number must between 1 to 1000")
    count+=1

print(f"Total takes={count}")




    

