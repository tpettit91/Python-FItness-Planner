# User Class
# Creates User Class for Fitness Planner project
# Todd Pettit 10/16/14 (Last edit 10/18/2014)


class User(object):
    """User Object Class"""
    user_list = []

    def __init__(self, username, gender, height, weight, age, activity):
        self.username = username
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age
        self.activity = activity
        self.bmr = -1       # placeholder value
        self.maint = -1     # placeholder value
        self.intake = -1    # placeholder value
        User.user_list.append(username)

    def __str__(self):
        rep = [self.username, self.gender, self.height, self.weight, self.age, self.activity]
        return str(rep)

if __name__ == "__main__":
    one = User("one", "m", 72, 190, 23, 4)
    print one
