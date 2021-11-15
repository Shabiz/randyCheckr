import random

print("Input how many times you'd like to run the RNG:")

input = int(input())

print(" ")

def randCyle(input):
    z = 0
    randomArray = []
    userList = [1,2,3,4,5,6,7,8,9,10]

    while z < input:
        randomNumber = random.randrange(1,11)
        randomArray.append(randomNumber)

        if len(randomArray) == input:
            for d in userList:
                if d not in randomArray:
                    print(str(d) + " 0 %")
                else:
                    percenty = randomArray.count(d)/input*100
                    print(d,percenty, "%")
            # uncomment this if you want to display the generated numbers print(randomArray)    

        z += 1

randCyle(input)
