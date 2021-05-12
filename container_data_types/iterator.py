numbers = [1,2,3,4,5]
# print(dir(numbers))

# it = iter(numbers)
# print(it)

# print(it.__next__())
# print(it.__next__())
# print(next(it))
# print(next(it))
# print(next(it))
# print(it.__next__())

# all dunder methods called be called as a normal function as well..
# eg: instead of it.__next__() we can also use next(it)

#custome iterator

# Fibonacci series: 0 1 1 2 3 5 8 13
class Fibonacci:
    
    def __init__(self, max):
        self.max = max
        self.prev = 0
        self.cur = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.prev < self.max:
            result = self.prev
            self.prev, self.cur = self.cur, self.prev+self.cur
            return result
        else:
            raise StopIteration
 
f = Fibonacci(35)
for i in f:
    print(i)
    
# it = iter(f)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
