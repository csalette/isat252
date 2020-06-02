"""
Lecture 9
"""

class car:  #car is class name
    
    maker = 'toyota'  #attribute
    #def report_maker(self):  #method
    def __init__(self,input_model):
        
        self.model = input_model
        
    def report(self):
        return self.maker,self.model
        
my_car = car('corolla')
print(my_car.report())

my_car.maker = 'ford'
print(my_car.report())
        
#my_corolla = car('corolla')
#print(my_corolla.maker)
#print(my_corolla.model)

#my_highlander = car('highlander')
#print(my_highlander.maker)
#print(my_highlander.model)
        
#my_car = car()  #create an instance/object
#print(my_car.maker)