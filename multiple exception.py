try:
    num1, num2 = eval(input("enter two numbers, seperated by a comma: "))
    result = num1/num2
    print("result is ", result)
except ZeroDivisionError as e:
    print("error: division by zero is not allowed.")
except Syntaxrror:
    print("comma is missing. Enter numbers seperated by comma like this 1, 2")
except:
    print("wrong input")
else:
    print("no exceptions")
finally:
    print("this will execute no matter what")
    
