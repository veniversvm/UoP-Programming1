# UoP Gym Python Mini Program

A simple interactive console program for gym membership registration.

## Functions

### `age_input() -> int`
Prompts the user to enter their age. Uses a `try/except` block inside an infinite `while True` loop to validate that the input is a valid integer. Continues prompting until a valid integer is entered.

### `training_program_selection(age: int) -> str`
Takes age as input and returns the appropriate fitness program:
- **Under 18** → Teen Fitness Program
- **18–39** → Regular Fitness Program
- **40+** → Senior Wellness Program

Uses defensive programming to validate the `age` parameter before proceeding.

### `has_medical_condition(age: int) -> bool`
Asks the user if they have a medical condition. Accepts `yes/y/no/n` as input. Returns `True` or `False` and prints relevant advice:
- Age 40+ with condition → recommends medical clearance
- Condition present → advises precaution
- No condition → allows proceeding

### `premium_membership(age: int, medical_condition: bool) -> (bool, int, bool)`
Handles premium membership selection:
- **Premium accepted** → plan = $60, includes personal trainer, applies youth discount if age < 30 and no medical condition
- **Premium declined** → asks about personal trainer:
  - With trainer → plan = $45
  - Without trainer → plan = $30
- Returns a tuple `(premium_status, plan_price, personal_trainer_flag)`

### `main()`
Orchestrates the full program flow:
1. Calls `age_input()` to get the user's age
2. Calls `training_program_selection()` to determine the program
3. Calls `has_medical_condition()` to check medical status
4. Calls `premium_membership()` to finalize the plan
5. Displays a summary of all selections

## Entry Point
The script runs `main()` when executed directly via `if __name__ == "__main__"`.
