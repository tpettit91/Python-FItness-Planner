# User Creator Func
#Func that creates a user
#Todd Pettit 10/16/14

import User


def check_username():
    username = ""

    while True:
        username = raw_input("Please enter a username to begin account creation")
        if username in User.User.user_list:
            print "This username already exists. Please try again."
        else:
            break
    create_user(username)


def create_user(username):
    """Func for requesting information and passing it into a user object"""
    print "welcome, ", username
    print "We're going to have to ask you a few questions in order to set up your account."
    gender = ""
    height = ""
    weight = ""
    age = ""
    activity = ""

    while True:
        gender = str(raw_input("Are you male (m), or female (f)?"))
        if gender != "m" and gender != "f":
            print "Invalid input: Please enter m for male, or f for female in the gender field."
        else:
            break

    while True:
        height = int(raw_input("What is your height in inches?"))
        if type(height) != int:
            print "Please enter your height in inches."
        else:
            break

    while True:
        weight = int(raw_input("What is your weight in pounds?"))
        if type(weight) != int:
            print "Please enter your weight in pounds."
        else:
            break

    while True:
        age = int(raw_input("How old are you?"))
        if type(age) != int:
            print "Please enter your age in years."
        else:
            break

    while True:
        activity = int(raw_input("""how active are you?
        Enter 1 for little to no exercise.
        Enter 2 for light exercise (1-3 days per week)
        Enter 3 for Moderate exercise (3 - 5 days per week)
        Enter 4 for Heavy Exercise (6 - 7 days per week)
        Enter 5 for Very heavy exercise (twice per day, extra heavy workouts)
        """))
        if activity not in range(0, 4, 1):
            print "Please enter number between 1 and 5 to represent your current activity level"
        else:
            break

    username = User.User(username, gender, height, weight, age, activity)


def stop_creating():
    while True:
        stop_creation = raw_input("Would you like to exit? y n")
        if stop_creation == "y" or stop_creation == "n":
            if stop_creation == "y":
                return "y"
            if stop_creation == "n":
                return "n"
        if stop_creation != "y" and stop_creation != "n":
            print "Please enter y or n"
        break


def main():
    check_username()

if __name__ == "__main__":
    stopper = ""
    while stopper != "y":
        main()
        stopper = stop_creating()
