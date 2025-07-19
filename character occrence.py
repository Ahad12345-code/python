string = input("please enter your own word: ")
char = input("please enter the chracter you want to count: ")
i = 0
count = 0
while(i < len(string)):
    if (string[i]== char):
        count = count + 1
    i = i +1
print("the character" , char,"occurs", count, "times in the world", string)


