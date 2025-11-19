class add:
    def __init__(self,item):
        self.item = item

    def __add__(self,b):
        newnumber = add(self.item + b)
        return newnumber
    def __call__(self,b):
        return self.__add__(b)
    def __str__(self):
        return str(self.item)
    def __repr__(self):
        return str(self.item)
addTwo = add(2)
print(addTwo + 5)
addTwo(3)
print(addTwo(3)(5))
