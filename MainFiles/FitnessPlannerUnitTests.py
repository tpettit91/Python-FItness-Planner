#Fitness Planner Unit Tests
#Unit tests for Fitness Planner functions
#Todd Pettit 10/29/2014
#----------------------------------------------------------------------------------------------------------------------#

import unittest
import calc


class CalcTest(unittest.TestCase):
    def test_bmr(self):
        """Unit Test verifying the calc_bmr function is working properly"""
        #Male imperial unit test
        unit    = "imperial"
        age     = 23
        weight  = 195
        height  = 72
        gender  = "m"
        result1 = calc.calc_bmr(unit, age, weight, height, gender)

        #Male metric unit test
        unit    = "metric"
        age     = 23
        weight  = 195 / 2.2046
        height  = 72 * 2.54
        gender  = "m"
        result2 = calc.calc_bmr(unit, age, weight, height, gender)

        #Female imperial unit test
        unit    = "imperial"
        age     = 23
        weight  = 130
        height  = 60
        gender  = "f"
        result3 = calc.calc_bmr(unit, age, weight, height, gender)

        #Female metric unit test
        unit    = "metric"
        age     = 23
        weight  = 130 / 2.2046
        height  = 60 * 2.54
        gender  = "f"
        result4 = calc.calc_bmr(unit, age, weight, height, gender)

        #Verify Male imperial == 2000, Male metric == 2000, and Male metric == Male imperial
        self.assertEqual(2000, result1)
        self.assertEqual(2000, result2)
        self.assertEqual(result1, result2)

        #Verify Female imperial == 1400, Female metric == 1400, and Female metric == Female imperial
        self.assertEqual(1400, result3)
        self.assertEqual(1400, result4)
        self.assertEqual(result3, result4)

    def test_maint(self):
        """Method confirms that calc_maint is working properly"""
        # activity level 2 example
        bmr      = 1400
        activity = 2
        result1  = calc.calc_maint(bmr, activity)

        # activity level 1 example
        bmr      = 2000
        activity = 1
        result2  = calc.calc_maint(bmr, activity)

        self.assertEqual(1900, result1)
        self.assertEqual(2400, result2)

    def test_intake(self):
        """Method verifies calc_intake function is working properly"""
        # 2 pounds loss per week example
        maint   = 1900
        goal    = "lose"
        change  = 2
        result1 = calc.calc_intake(maint, goal, change)

        # 1 pounds gain per week example
        maint   = 2000
        goal    = "gain"
        change  = 1
        result2 = calc.calc_intake(maint, goal, change)

        self.assertEqual(900, result1)
        self.assertEqual(2500, result2)

    def test_max(self):
        """Method verifies calc_maximum function is working as expected."""
        reps    = 10
        weight  = 100
        result1 = calc.calc_maximum(reps, weight)

        self.assertEqual(133, result1)

if __name__ == "__main__":
    unittest.main()
