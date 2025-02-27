#find factorial
#Take user_input
data = int(input("Enter no for factorial::"))
#Using for loop to find factorial
fact =1
for i in range(1, data+1):
    fact = fact * i
print("factorial using for loop: ",fact)
#using recursion function to find factorial
def recurstion_test(a):
    if a < 2 :
        return 1
    else :
        return a * recurstion_test(a-1)

result = recurstion_test(data)
print("factorial using recursion function:",result)