a=10

# def test():
#     global a
#     a=20
#     print(f"local : {a}")

# test()
# print(f"global : {a}")





# def test():
#     global a
#     a=20
#     print(f"local : {a}")

def test():
    a=20
    x=globals()['a']
    print(f"local : {a}")
    x=30
    print(f"local : {x}")
    globals()['a'] = 15
    print(f"local : {a}")


test()
print(f"global : {a}")