L =[23,1,0,-12,48, 15, 9, 20, -11, 42,7, -5, 13]

# Every Second
for i in range(len(L)):
    if i % 2 == 1:
        print(L[i])

# Sum
sum = 0
for i in L:
    sum += i
    
print("sum:", sum)

# 1 - 10000 inclusive Commented out because it takes a long time to run
#for i in range(1, 10001):
    #print(i)

string = "Code Happy"
for i in string:
    print(i)
    
# Rectangle
length = float(input("Length: "))
width = float(input("Width: "))
print("Area: ", length * width)

# Program 6
answer = ""
while answer != "z":
    answer = input("Enter z or Z: ").lower()

# Program 7
file1 = open("CS04022022.txt", "w")
file1.write("""Leunig –How To Get There
Go to the end of the path until you get to the gate.
Go through the gate and head straight out towards the horizon.
Keep going towards the horizon.
Sit down and have a rest every now and again,
But keep on going, just keep on with it.
Keep on going as far as you can.
That is how you get there.""")
file1.close()

