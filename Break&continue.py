#Break and Continue Statement
 #Break = Used to terminate the loop when encounted
# Continue = terminates execution  in the current iteration & continue exceution in the loop  


# Example of brak Statment
i=1
while i<=5:
    print(i)
    if(i == 3):
        break
    i += 1
   print("end of the loop")


  #   Example of continue statment
i = 0
while i<= 5:
    if(i == 3):
        i += 1
       continue
    print(i)
    i += 1

# WAP print the odd number by using loop 
i = 1
while i <= 10:
        if(i%2 == 0):
         i += 1 
       continue
print(i)
i += 1
   # Write a prgorame by using whiel loop 
i=1
while i<=10:
    if(i%2 == 0):
     continue
   print(i)
    i
   
# Range = range function returns in sequence of number starting from 0 by default and increment by 1 (by default) , and stops before specifeid number.
seq = range(5)
for i in seq:
   print(i)
 
  range 
for i  in range(2,10): #range(start,stop)
 print(i)
 
#for i in range(10): # range(start)
 #    print(i)
# example of range in the programming language 
for i in range(1,10,3):  
  range(start,stop,step)
    print(i)
 
 # print the number from 1 to 100
 #solution 
  for i in range(1,101)
    print(i)

# print the number from 100 to 1 
# solution:
for i in range(100,0,-1):
print(i)

# Print the multiplication table of a number n 
n = int(input("Enter the number:"))
for i in range(1,11):
 print(n*i)
 
 # Pass Statement = Pass is null statement that does nothing . It is used as a placeholder for future code 
 # WAP to find the sum of first n natural number by using for loop
n = 5
sum = 0 
for i in range(1,n+1):
    sum += i
    print("total sum =", sum)
    print(i)
    
# WAP to find  the sum of first n number (using while 
n = 7 
sum = 0
i = 1 
while i<=n:
    sum += i
    i += 1 
    print("total sum", sum )

# WAP to find the factorial of first n number(using for loop)
n = 5 
fact = 1 
i = 1 
while i<=n:
fact *= i
i += 1 
print("factorial =", fact)
a = 10
b = 20
print(a+b)

# input statement in the python programming
num1 = input(num1)
num2 = input(num2)


