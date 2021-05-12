def fibonacci(limit):
    prev, cur = 0, 1
  
    while prev < limit:
        yield prev
        prev, cur = cur, prev + cur
  
x = fibonacci(5)
  
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

# for i in fibonacci(35):
#     print(i)