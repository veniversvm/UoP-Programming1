import unittest

# Global variable for the daily step goal (demonstrates variable scope)
avg_goal = 100

def calculate_average(value: int, days: int = 7) -> float:
    """
    calculate_average takes two arguments,
    first the number of given steps/calories/minutes and the second
    is optional with a default value of '7'.

    Any zero value will automatically return 0.

    Any negative value will raise a ValueError.
    """
    if value == 0 or days == 0: 
        return 0
    if value < 0 or days < 0: 
        raise ValueError("steps and days can't be negative")
    
    # Returns rounded to 2 decimal places, as implied by the tests
    return round(value / days, 2)

def average_accomplished(avg: float) -> bool:
    """
    average_accomplished takes the average number of 
    steps and checks against the 'avg_goal' global variable.
    """
    global avg_goal
    return avg >= avg_goal

def display_summary(total_steps: int, total_calories: int, total_minutes: int, days: int = 7) -> None:
    """
    Calculates and displays the performance summary using the custom functions,
    avoiding code repetition.
    """
    avg_steps = calculate_average(total_steps, days)
    avg_calories = calculate_average(total_calories, days)
    avg_minutes = calculate_average(total_minutes, days)
    
    goal_met = average_accomplished(avg_steps)
    
    print("--- Weekly Fitness Summary ---")
    print(f"Average Steps per Day: {avg_steps}")
    print(f"Average Calories Burned per Day: {avg_calories}")
    print(f"Average Minutes of Exercise per Day: {avg_minutes}")
    print(f"Step Goal Met (Goal: {avg_goal}): {'Yes' if goal_met else 'No'}")
    print("------------------------------")

def main() -> None:
    # Test data to simulate a week of exercise
    weekly_steps = 850
    weekly_calories = 2100
    weekly_minutes = 350
    
    # Calls the function that groups the logic instead of repeating code
    display_summary(weekly_steps, weekly_calories, weekly_minutes)


if __name__ == "__main__":
    main()
    
# ==========================================
#                  TEST
# ==========================================

class Test(unittest.TestCase):
    """
        Tests are really useful to prove the correctness 
        and functionality without manual testing.
    """
    def test_calculate_average(self):
        # Verifies that the function correctly calculates standard averages.
        self.assertEqual(calculate_average(21), 3.0, "should be '3.0'")
        self.assertEqual(calculate_average(50), 7.14, "should be '7.14'")
    
    def test_should_raise_value_error(self):
        # Ensures that passing a negative value for 'value' triggers a ValueError.
        # The 'with' statement safely catches the error so the test can pass instead of crashing.
        with self.assertRaises(ValueError) as context:
            calculate_average(-5, 21) 
        self.assertEqual(str(context.exception), "steps and days can't be negative")
        
        with self.assertRaises(ValueError) as context:
            calculate_average(5, -21) 
        self.assertEqual(str(context.exception), "steps and days can't be negative")

    def test_should_return_zero(self):
        # Tests edge cases (zeroes) to ensure the program doesn't crash with a ZeroDivisionError
        self.assertEqual(calculate_average(0, 0), 0, "should return '0'")
        self.assertEqual(calculate_average(10, 0), 0, "should return '0'")
        self.assertEqual(calculate_average(0, 2), 0, "should return '0'")

    def test_average_accomplished(self):
        # Verifies the boundary condition: when the average is exactly equal to the goal (100)
        self.assertTrue(average_accomplished(100), "Should return True when average meets the goal exactly")
        
        # Verifies when the average is well above the goal
        self.assertTrue(average_accomplished(150), "Should return True when average exceeds the goal")
        
        # Verifies when the average is strictly below the goal
        self.assertFalse(average_accomplished(99.9), "Should return False when average is just below the goal")
        self.assertFalse(average_accomplished(50), "Should return False when average is significantly below the goal")