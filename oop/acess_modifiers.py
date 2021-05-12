class Test:
    def __init__(self):
        self.foo = 2
        self._bar = 123
        self.__baz = 1234


print(dir(Test))


# it applies to class name , method names as well.. just a hint to developer, not strict imposition by the compiler
