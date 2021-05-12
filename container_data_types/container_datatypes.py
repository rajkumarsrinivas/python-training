from collections import deque

str="rajkumar"

# print(type(str))

# str=134
# print(type(str))

employee = {
    "name" : "raj",
    "age" : 73,
    "salary" : 10000
}

list=["wow", 34, employee, 3.25]

# for l in str:
#     print(l)


# print(type(set))
# set={"raj", 34, "raj", "age"}

# for s in set:
#     print(s)

# for k,v in employee.items():
#     print(f"{k} --> {v}")

# tuple=("wow", 34, employee, 3.25)

# for k in tuple:
#     print(k)



#Sorting.

employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

 
# sort by name (Ascending order)
# employees.sort(key=lambda x: x['Name'])
# print(employees, end='\n\n')

# sort by Age (Ascending order)
# employees.sort(key=lambda x: x.get('age'))
# print(employees, end='\n\n')

# # sort by salary (Descending order)
# employees.sort(key=lambda x: x['salary'], reverse=True)
# print(employees, end='\n\n')


#STACK
# stack = ["Raj", "Saurabh"]
# print(stack)
# stack.append("Banu")
# stack.append("Bonie")
# print(stack)

# #Removes element from last 
# print(stack.pop())
  
# print(stack)
  

# QUEUE
# queue = ["Raj", "Saurabh"]
# queue.append("Banu")
# queue.append("Bonie")
# print(queue)
  
# #Removes element from first
# print(queue.pop(0))
  
# print(queue)



queue = deque(["Raj", "Saurabh", "Banu", "Bonie"])
print(queue)
queue.append("Alex")
queue.append("Michael")
print(queue)

print(f"stack --> pop --> {queue.pop()}")
print(queue)


print(f"queue --> pop --> {queue.popleft()}")
print(queue)
