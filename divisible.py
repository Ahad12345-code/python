print("enter a number(numerator):")
num=int(input())
print("enter a number(denominator):")
denom=int(input())
if num%denom ==0:
    print("n/"+ str(num)+"is divisible by"+ str(denom))
else:
    print("n/"+ str(num)+"is not divisibleby"+ str(denom))
