#If statement:

x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
#For loop:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
 print(fruit)

#While loop:
print("while")
count = 0
while count < 5:
    print(count)
    count += 1
#Break statement:
print("Break statement")
for i in range(10):
    if i == 5:
        break
    print(i)
#Continue statement:
print("Continue statement")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
#Pass statement:
print("Pass statement")
x = 10
if x > 0:
    pass  # Placeholder, do nothing for now
else:
    print("x is negative")


