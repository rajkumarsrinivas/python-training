# str1='hi, how are you str1'
# print(str1, end='\n')
# # print("hello world")

# str2="hi, how are you str2"
# print(str2, end='##')

# str3="""hi, 
# how are you str3"""
# print(str3, end='\n\n')

# str4='''hi, 
# how are you str4'''
# print(str4, end='\n$$')

name="raj"
age=73
# print("i am %s & my age is %s" % (name, age), end='\n\n')


# print("i am {} & my age is {}".format(name, age), end='\n\n')

print("i am {1} & my age is {0}".format(age, name), end='\n\n')

print("i am {nam} & my age is {ag}".format(nam=name,ag=age), end='\n\n')

# person ={"name":"raj", "age":73}
# print("i am {name} & my age is {age}".format(**person))


print(f"i am {name} & my age is {age}")

# public boolean test(String abc) {
#     if(abc != null) {
#         return True
#     }
#     return False
# }

# def test(abc):
#     if abc is not None:
#         return True
#     return False


