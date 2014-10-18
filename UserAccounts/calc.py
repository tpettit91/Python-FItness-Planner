# Calculator Module
# Performs calculations for BRM, Caloric Intake, 1RM, and Macros
# Todd Pettit 10/17/2014
import User


# Test Case User class
class User(object):
    def __init__(self, username, gender, height, weight, age, activity):
        self.username = username
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age
        self.activity = activity
        self.bmr = ""
        self.maint = ""
        self.intake = ""


def calc_bmr(user):
    """Calculating calories burned simply by existing."""
    calc_age = user.age
    calc_weight = user.weight
    calc_height = user.height
    calc_gender = user.gender
    # Metric Conversions
    calc_weight /= 2.2046
    calc_height *= 2.54
    # Determining gender and performing calculations
    if calc_gender == "m":
        bmr = 88.362 + (13.397 * calc_weight) + (4.799 * calc_height) - (5.677 * calc_age)
        return bmr
    if calc_gender == "f":
        bmr = 447.593 + (9.247 * calc_weight) + (3.098 * calc_height) - (4.330 * calc_age)
        return bmr


def calc_maint(user):
    """calculating suggested calories for weight maintenance taking activity into account"""
    bmr = user.bmr
    act_dict = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}
    adj = act_dict[user.activity]
    maint_cal = bmr * adj
    return maint_cal


def calc_intake(user):
    """Adjusting Caloric intake for weight goals"""
    maint = user.maint
    weight_goal = ""

    while True:
        weight_goal = int(raw_input("Do you want to lose weight or gain weight? 1 for lose 2 for gain"))
        if weight_goal == 1 or 2:
            break
        else:
            print "Please enter 1 for weight loss and 2 for weight gain"
    if weight_goal == 1:
        change_goal = int(raw_input("How many pounds per week? For weight loss no more than 2 is suggested."))
        change_goal *= 500
        intake_sug = maint - change_goal
        return intake_sug
    if weight_goal == 2:
        change_goal = int(raw_input("How many pounds per week? For weigh gain no more than 1 is suggested."))
        change_goal *= 500
        intake_sug = maint + change_goal
        return intake_sug


def calc_max():
    """Calculate the one rep mex of a lift"""
    #This shit doesn't fucking work
    reps = ""
    weight = ""
    while True:
        reps = int(raw_input("How many reps did you perform?"))
        if type(reps) == int:
            break
        else:
            print "Please enter a valid number for the number of reps you performed"
    while True:
        weight = int(raw_input("How much weight did you use?"))
        if type(weight) == int:
            break
        else:
            print "Please enter a valid number for the weight you used."
    print weight * (1 + reps / 30)
    maximum = weight * (1 + reps / 30.0)
    return maximum


def main():
    test1 = User("test1", "m", 72, 190, 23, 4)
    test1.bmr = calc_bmr(test1)
    test1.maint = calc_maint(test1)
    test1.intake = calc_intake(test1)
    print test1.bmr
    print test1.maint
    print test1.intake
    print calc_max()


#Main loop for testing
if __name__ == "__main__":
    main()
