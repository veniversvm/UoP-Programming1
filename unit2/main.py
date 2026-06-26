### UoP GYM Py Mini Program ###

"""
    Functions
    Allows us to reunite the code in smaller logical blocks.
    Functions in Python starts with 'def' keyword like this:

        def some_function(age: int, medical_condition):
            # some logic
            return some_value

    and are invoked like this:

        some_function(age, medical_condition)
"""

def age_input() -> int:
    print("Please insert your age: ")
    while True:
        try:
            """
            This is a valid expression for the goal of obtaining
            the age:

            age_input = input()
            age_int   = int(age_input)
            return age_int

            """

            # But the expression can be summarized into one line
            # This expression tries to convert the input and return
            # the value in one sentence, but if fails will return nothing.
            return int(input()) 
        except ValueError as e:
            # Non valid values are catched in the except.
            print(e)
            print("--- PLEASE INSERT A VALID INPUT ---\n")

######
######
######

def training_program_selection(age: int) -> str:
    # Check if the value 'age' is valid.
    # This is called Defensive Programming.
    if not isinstance(age, int) or age <= 0:
        return ValueError(f"""
   ---  Invalid Age Parameter ---
        Obtained: {age} as {type(age)}
        Must be an integer value greater than zero (0)\n
        """)
    # Just a clean space
    print("")
    if age < 18:
        return "* - You are eligible for the Teen Fitness Program."
    elif age < 40:
        return "* - You are eligible for the Regular Fitness Program."
    else:
        return "* - You are eligible for the Senior Wellness Program."
    """
    The upper If/Else block can be written also as:

    if age < 18: # The early return shortcircuit the evaluation
        return  "You are eligible for the Teen Fitness Program."
    if age < 40: # Same as above
        return "You are eligible for the Regular Fitness Program."
    # This block only runs if the previous one doesn't get executed
    return "You are eligible for the Senior Wellness Program."

    """

######
######
######

def has_medical_condition(age: int) -> bool:
    # Again Defensive Programming
    # We can put this block on a new function but for now
    # I prefer to keep some simplicity for newcomers in programming.
    if not isinstance(age, int) or age <= 0:
        return ValueError(f"""
   ---  Invalid Age Parameter ---
        Obtained: {age} as {type(age)}
        Must be an integer value greater than zero (0)
        """)
    input() # A little pause to not print info immediately
    condition_response = None # Init of variable in upper scope
    print("Do you have any medical condition? (Y/n)")
    
    """
        There are more efficient ways to write this block.
        I maintain some simplicity for newcomers.
    """
    while True:
        condition_input = input()
        condition_response = condition_input.lower()
        if condition_response in ("yes", "y", "no", "n"):
            break
        else:
            print("Invalid value, please use 'Yes' or 'No' options")
    # expression return a boolean value that can be stored
    has_condition: bool = condition_response in ("yes", "y")

    if age >= 40 and has_condition:
        print("Medical clearance required before joining.")
    elif has_condition:
        print("Please take precaution")
    else:
        print("You can proceed with registration.")
    return has_condition


######
######
######

def premium_membership(age: int, medical_condition: bool) -> (bool, int, bool):
    # Initializes membership variables with default values
    premium = False
    plan = None
    personal_trainer = False
    input() # A little pause to not print info immediately
    print("Do you want Premium Membership? (Y/n)")

    # Loop until valid input is received
    while True:
        premium_input = input()
        premium_response = premium_input.lower()
        # User accepts premium membership
        if premium_response in ("yes", "y"):
            premium = True
            personal_trainer = True
            plan = 60  # Premium plan price
            # I don't like nested conditions xP
            if age < 30 and not medical_condition:
                print("* - You qualify for a youth discount! 10% off your plan")
            if medical_condition:
                print("* - We recommend a free consultation before starting.")
            break
        # User declines premium membership
        elif premium_response in ("no","n"):
            print("Do you want a Personal Trainer? (Y/n): ")
            personal_trainer = input()
            # Insecure section but I don't want to over complicate
            # the code
            personal_trainer_response = premium_input.lower()
            # User wants a personal trainer on a standard plan
            if personal_trainer_response in ("yes", "y"):
                plan = 45  # Standard plan with trainer price
                personal_trainer = True
                break
            else:
                plan = 30  # Basic plan price
                print("* - Consider upgrading to Premium for more benefits!")
                break
        else:
            print("Invalid value, please use 'Yes' or 'No' options")

    input() # Pause before returning to the main menu
    # Returns a tuple with: premium status, plan price, and personal trainer flag
    return (premium, plan, personal_trainer)

######
######
######

def main():
    print("--- Welcome to UoP Fitness Gym ---")
    age: int = age_input()
    training_program = training_program_selection(age)
    print(training_program)
    med_condition = has_medical_condition(age)
    type_plan, value_plan, trainer = premium_membership(age, med_condition)
    print(f"Plan Value {value_plan}$")

    print(f"""
 - Age              : {age}
 - Training Program : {training_program}
 - Medical Condition: {"Yes" if med_condition else "None"}
 - Personal Trainer : {"Yes" if trainer else "None"}
 - Amount           : {value_plan}$
    """)

    input()
if __name__ == "__main__":
    main()
