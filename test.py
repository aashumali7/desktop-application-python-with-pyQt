class SecondClass():
     

     #3.
     def addMenu(self,menuTitle):
         print("Calculator")
    
class Aashish():
    #1.property

    #2. constructor

    #3. method

    def menuBar(self):
        print("menubar is calling")  
        co2 = SecondClass()
        return co2
    pass 

co = Aashish()
mb = co.menuBar()
print(mb.addMenu("Calculator"))