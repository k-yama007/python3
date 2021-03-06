class Mapping:
    def __init__(self,iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self,iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update # private copy of original updatted() method

class MappingSubclass(Mapping):

    def update(self,keys,values):
        #provides new signature for update()
        #but does not break __init__()
        for item in zip(keys,values):
            self.items_list.append(item)


class Employee:
    pass


john = Employee() #Create an empty employee record

#Fill the fields of the record
john.name = 'John Doe'
john.dept='computer lab'
john.salary = 1000



print("name:",john.name)
print("Dept:",john.dept)
print("salary:",john.salary)

for element in [1,2,3]:
    print(element)
for element in (1,2,3):
    print(element)
for key in {'one':1,'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line,end='')
    
