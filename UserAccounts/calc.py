# Calculator Module
# Performs calculations for BRM, Caloric Intake, 1RM, and Macros
# Todd Pettit 10/17/2014
import User


def calc_bmr(age, weight, height, gender):
    """Calculating calories burned simply by existing."""
    # Metric Conversions
    weight /= 2.2046
    height *= 2.54
    # Determining gender and performing calculations
    if gender == "m":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        return bmr
    if gender == "f":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        return bmr


def calc_maint(bmr, activity):
    """calculating suggested calories for weight maintenance taking activity into account"""
    act_dict = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}
    adj = act_dict[activity]
    maint_cal = bmr * adj
    return maint_cal


def calc_intake(maint):
    """Adjusting Caloric intake for weight goals"""
    weight_goal = -1

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
    reps = -1
    weight = -1
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
    maximum = weight * (1 + reps / 30.0)
    return maximum


def main():
    test1 = User.User("test1", "m", 72, 190, 23, 4)
    test1.bmr = calc_bmr(test1.age, test1.weight, test1.height, test1.gender)
    test1.maint = calc_maint(test1.bmr, test1.activity)
    test1.intake = calc_intake(test1.maint)
    print "customer bmr: ", test1.bmr
    print "customer maint: ", test1.maint
    print "customer suggested intake: ", test1.intake
    print calc_max()


#Main loop for testing
if __name__ == "__main__":
    main()
