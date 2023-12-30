#1class defination
class Parent():
    #property

    #constructor

    #method
    def setWindowTitle(self, title):
        print(f'title is {title}')

    pass
class Child(Parent):
    #property

    #constructor
    def __init__(self): #self is cio class internal object
        self.setupUi()
    #method
    def setupUi(self):
        print('hello from setup method')
        pass
    
    def aashish(self):
        print('hello from aashish method')
    pass

#2 create class object
ceo = Child() #ceo is Class external object
ceo.aashish()