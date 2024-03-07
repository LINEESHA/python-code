x = lambda a : a + 20
print(x(5))

x = lambda a, b, c : a + b + c
print(x(20, 30, 20))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(5)
mytripler = myfunc(5)

print(mydoubler(11))
print(mytripler(11))