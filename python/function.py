def banu(x,y): # parameter nothing but variable
    print(x+ " "+y)
banu("pink","yellow") # agruments nothing give value for variable


# for and while
numbers=[1,2,3,4,5,6,7,8,9,10]
for x in numbers:
    print(x)
    if x == 5:
        break
print("br and cont ")
m=[1,2,3,4,5,6,7,8,9,10]
for l in m:
       if l == 6:
            continue
       print(l)
# while
print("while")
i=1
while i<6:
     print(i)
     if i==3:
         break
     i+=1
# function as arguments
list=["car","bikes"]
def priya(x):
    print(x*3)
def m(crazy,list):
    for iteam in list:
        crazy(list)

m(priya,list)

# list
j=['banu',8,8.9,True,'car','banu']
j[5]='priya'
j.insert(4,"cars")
j.append("elements")

print(j)
#string
amount=0
print(amount)
amount=amount+4
if amount>0:
    print("if its not zero")
mul=" banu"*4
print(mul)