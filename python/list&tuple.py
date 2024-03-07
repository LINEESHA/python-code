# list is changable have can duplicate
lists=[1,2,3,4,5,6,7,8]#list
lists.insert(0,10)
print(lists)
m=("car","bike",1,3.0)#tuple
print(m)
#once option to change duple to list then change the value of it
b=("car","bike",1,3.0)
y=list(b)
y[1]="örange"
x=tuple(y)
print(x)
#create a calendar
import calendar
y=2024
m=1
print(calendar.month(y,m))

#.............
year=2023
for m in range(1,13):
    print(calendar.month(y,m))

from itertools import permutations

characters=['a','b','c']
# combination of three characters
unique_character=set(permutations(characters, 3))
for combo in unique_character:
     print(' '.join(combo))

     # combination of two characters
     unique_character = set(permutations(characters, 2))
     for combo in unique_character:
          print(' '.join(combo))









