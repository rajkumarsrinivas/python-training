#comprehension

fruits = ['apple', 'orange', 'watermelon', 'banana', 'guava', 'kiwi', 'lemon', 'berry']
# for i,v in enumerate(fruits):
#     print(f"{i} --> {v}")
# list comprehension
# prepare a list of numbers from 0 to 9.
# prepare a list of even numbers
# def list():
#     # num = []
#     # for i in range (10):
#     #     num.append(i)
#     # print(num)
#     num = [x*x for x in range(10)]
#     print(num)
# list()

#cartesian product {1,2,3}x{2,3} => {(1,2), (1,3), (2,2), (2,3), (3,2), (3,3)}
# def cartesian():
    # print("{", end="")
    # for i in range(1, 5):
    #     for j in range(1,5):
    #         #print(f"({i}, {j})")
    #         #print(i,j, sep="*", end=" $ ")
    #         print(f"({i}, {j})", end=",")
    # print("}")
    # l = [(x , y) for y in range(1, 5) for x in range(1,5) if x != y]
    #  l = [(x, y) for x in range(1,5) for y in range(x+1, 5)]
    #  print(l)


#nested list
# cartesian()
# def cartesian():
    # for i in range(1, 5):
    #     for j in range(i,5):
    #         print(f"({i}", f"{j})", sep=",")
#     l = [[(x , y) for y in range(x, 5)] for x in range(1,5)]
#     print(l)
# cartesian()

# def board():
    # b = [str(x) for x in range(9)]
    # for row in [b[i*3:(i+1)*3] for i in range(3)]:
    #     print('| '+' | '.join(row)+' |')
    # print()
    # print("####################")
    # print()

#     b=[[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
#     for h in b:
#         print('| '+' | '.join(h)+' |')

# board()


# set comprehension
# def set_compre():
#     l = [1,1,1,3,4,2,5,4,3]
#     s = {x for x in l}
#     print("set ==> "+str(s)) 
# set_compre()

#dict comprehension
m = {x: x**2 for x in (2, 4, 6)}
print(m)