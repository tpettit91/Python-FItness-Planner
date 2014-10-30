#Modified user class
#user class for initial site configuration
#Todd Pettit 10/25/2014
#----------------------------------------------------------------------------------------------------------------------#


class User(object):
    """User Object Class"""
    def __init__(self, first_name, last_name, gender, height, weight, age):
        self.first_name = first_name
        self.last_name  = last_name
        self.gender     = gender
        self.height     = height
        self.weight     = weight
        self.age        = age

    def __str__(self):
        print self.first_name, self.last_name, self.gender, self.height, self.weight, self.age

