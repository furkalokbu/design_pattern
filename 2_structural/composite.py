class Component(object):
    """Abstract class"""
    def __init__(self, *args, **kwargs):
        pass

    def component_function(self):
        pass

class Chield(Component): #Inherios from abstract class, Component
    """Concrete class"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        #This is where we store the name of your child item!
        self.name = args[0]

    def component_function(self):
        #Print the name of your child item here!
        print('{}'.format(self.name))


class Composite(Component): #Inherios from abstract class, Component
    """Concrete class and maintains the tree recursive structure"""

    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)

        #This is where we store the name of the composite object
        self.name = args[0]

        #This is where we keep our child items
        self.children = []

    def append_child(self, child):
        """Method to add a new child item"""
        self.children.append(child)

    def remove_child(self, child):
        """Method to remove a child item"""
        self.children.remove(child)

    def component_function(self):

        #Print the name of the composite object
        print('{}'.format(self.name))

        #Iterate through the child objects and invoke their component function printing their names
        for i in self.children:
            i.component_function()

#Build a composite submenu1
sub1 = Composite("submenu1")
sub11 = Chield("sub_submenu11")
sub12 = Chield("sub_submenu 12")

#Add the sub_submenu 11 to submenu 1
sub1.append_child(sub11)
#Add the sub_submenu 12 to submemu 1
sub1.append_child(sub12)

#build a top level composite menu
top = Composite("top_menu")

#build a submenu 2 that is not a composite
sub2 = Chield("submenu2")

#add the composite submenu 1 to the top-level composite menu
top.append_child(sub1)

#add the composite submenu 2 to the top-level composite menu
top.append_child(sub2)

#Let's test if our Composite parrent works!
top.component_function()