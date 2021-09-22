class House(object):
    def accept(self, visitor):
        """Interface to accept a visitor"""
        #Triggers the visiting operation!
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, "worked on by", hvac_specialist) #Note that we now have a reference to the HVAC specialist object in the house object!
    
    def work_on_electricity(self, electrician):
         print(self, "worked on by", electrician) #Note that we now have a reference to the electrician object in the houser object! 

    def __str__(self):
        """Simply return the class name when the House object is printed"""
        return self.__class__.__name__

class Visitor(object):
    """Abstract Visitor"""
    def __str__(self):
        return self.__class__.__name__

class HvacSpecialist(Visitor):
    """Concrete visitor: HVAC specialist"""
    def visit(self, house):
        house.work_on_hvac(self)

class Electrician(Visitor):
    def visit(self, house):
        #Note that the visitor now has a reference to the house object
        house.work_on_electricity(self)

#Create an HVAC specialist
hv = HvacSpecialist()
#Create an electrician
e = Electrician()

#Create a house
home = House()

#Let the house accept the HVAC specialist and work on the house by invoking the visit() method
home.accept(hv)

#Let the house accept the electrician and work on the house by invoking the visit() method
home.accept(e)

