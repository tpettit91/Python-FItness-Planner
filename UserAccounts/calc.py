#Fitness Planner Calculator
#Performs Calculations
#Todd Pettit 10/25/2014
#----------------------------------------------------------------------------------------------------------------------#


def convert_pounds(pounds):
    """Converts pounds to kilograms"""
    pounds /= 2.2046
    return pounds


def convert_inches(inches):
    """Converts Inches to Centimeters"""
    inches *= 2.54
    return inches


def calc_bmr(unit, age, weight, height, gender):
    """Calculating calories burned simply by existing."""
    if unit == "imperial":
        weight = convert_pounds(weight)
        height = convert_inches(height)

    # Determining gender and performing calculations
    if gender == "m":
        bmr = 66.0 + (13.7 * weight) + (5.0 * height) - (6.8 * age)
        return round(bmr, -2)
    if gender == "f":
        bmr = 655.0 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
        return round(bmr, -2)


def calc_maint(bmr, activity):
    """calculating suggested calories for weight maintenance taking activity into account"""
    act_dict  = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.725, 5: 1.9}
    adj       = act_dict[activity]
    maint = bmr * adj
    return round(maint, -2)


#goal should be gain or lose, change should be a positive int representing the pounds of change per week
def calc_intake(maint, goal, change):
    """Adjusting Caloric intake for weight goals"""
    if goal == "gain":
        intake = maint + change * 500
        return intake
    if goal == "lose":
        intake = maint - change * 500
        return intake


def calc_maximum(reps, weight):
    """Calculate the one rep mex of a lift"""
    maximum = weight * (1 + reps / 30.0)
    return round(maximum)

if __name__ == '__main__':
    print calc_bmr("imperial", 23, 130, 60, "f")
    print calc_bmr("imperial", 23, 195, 72, "m")
