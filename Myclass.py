class Myclass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
    


class Dog:

    kind = 'canine'    #class variable shared by all instances
    tricks = []
    def __init__(self,name):
        self.name = name    #instance variable unique to each instance
    
    def add_trick(self,trick):
        self.tricks.append(trick)



def __init__(self):
    self.data=[]

x=Myclass()
y=Myclass


print("x=Myclass()")
print("Myclass():",x)
print("Myclass.f:",x.f)
print("Myclass.f():",x.f())
print("Myclass.i:",x.i)
print("y=Myclass:",y)

#9.3.3. インスタンスオブジェクト
x.counter =1

while x.counter <10:
    x.counter = x.counter +2
print("x.counter : ",x.counter)
del x.counter

#9.3.5. クラスとインスタンス変数
d= Dog('Fido')
e= Dog('Buddy')

d.add_trick('roll over')
e.add_trick('play dead')

print("kind of Dog:",d.kind)
print("kind of Dog:",e.kind)
print("name of Dog:",d.name)
print("name of Dog:",e.name)

print(d.tricks)  #unexpectedly shared by all dogs


if __name__ == "__main__" :
    import sys

    