class Square:
    def __init__(self, size):
        self.__size = size
try:
    print(mysquare.size)
except Exception as e:
    print(e)

try:
    print(mysquare._Square__size)
except Exception as e:
    print(e)
    
mysquare = Square(3)
print(type(mysquare))
print(mysquare.__dict__)
