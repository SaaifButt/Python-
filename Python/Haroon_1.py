"""Ask user to input two numbers in two different variables
If the sum of those number is greater than 10
Print "sum is greater than 10"
If the number is less than 10 print sum is less than 10
If sum is = to 10 print sum is equal to (the value of sum)"""

x = float(input("First number:"))
y = float(input("Second number:"))
if x + y > 10 :
    print('sum is greater than 10')
elif x + y < 10 :
    print('sum is less than 10')
elif x + y == 10 :
    print ('Sum is equal to the value of sum')
