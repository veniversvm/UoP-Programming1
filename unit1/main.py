### General coffee list ###
# This list holds all the coffee items available on the menu.
# Each coffee is stored as a dictionary with its name, price, and availability.
COFFE_LIST: list[dict] = [
    {
        "name": "Cappuccino",
        "price": 3.50,          # Price can be a float if it includes cents
        "available": True,      # True means the coffee can be ordered
    },
    {
        "name": "American",
        "price": 1,             # Integer price is allowed; Python handles the math automatically
        "available": True,
    },
    {
        "name": "Machiato",
        "price": 2.15,
        "available": False,     # This coffee is currently out of stock
    },
]

# This is a comment, it is no processced by the runtime
"""
    This is a multiline comment.
"""

"""
    def some_name():
        some code....

    That is a function, is an easy way to group code that has a particular objetive
    in one block. ALso can be called as many times as you want.
"""

### Inner functions ###
def _print_coffe_list(len_coffe: int) -> None:
    """Display the numbered menu list with prices."""
    # Loop through each coffee in the list up to the given length
    for i in range(len_coffe):
        # Print the index (starting at 1), name, and price
        print(f"{i+1} - {COFFE_LIST[i]["name"]} --- Price: {COFFE_LIST[i]["price"]}$")
    print(" ")  # Blank line for readability


def _get_number(limit: int) -> int:
    """Ask the user for a number between 1 and 'limit', keep asking until valid."""
    while True:  # Infinite loop until we get a valid number
        n = input()              # Read user input as a string
        try:
            n = int(n)           # Try to convert it to an integer
            if n < 0 or n > limit:
                print("Please use a valid option.")
            else:
                return n         # Valid number, exit the function
        except ValueError:       # If the input wasn't a number at all
            print(f"Please use only numbers from 1 to {limit}.")


def _yes_or_not(msg: str) -> bool:
    """Ask a yes/no question and return True for yes, False for no."""
    if isinstance(msg, str):
        print(msg)               # Print the custom question if provided
    else:
        print("Yes (y) or No (n): ")  # Default prompt
    r = input()                  # Get the answer
    # Convert to lowercase and check if it matches common yes responses
    return r.lower() in ["yes", "y"]


def _how_namy_coffes(coffe_name: str = "coffe") -> int:
    """Ask how many cups of a specific coffee the customer wants."""
    print(f"How many {coffe_name}s do you want?: ")
    # Use _get_number to ensure a valid number between 1 and 100
    return _get_number(100)


### External Function ###
def get_name() -> str:
    """Ask for the customer's name and validate that it contains only letters."""
    print("Welcome to Marvelous Cafe\nCan give me your name?: ")
    while True:
        name: str = input()
        # Check that the name is a string and contains only alphabetic characters (after stripping spaces)
        if isinstance(name, str) and name.strip().isalpha():
            return name
        else:
            print("Invalid name, you can only use 'letters' in name: ")


def get_order() -> list[dict]:
    """Interactively build the customer's order by selecting coffees and quantities."""
    selected_coffes: list[dict] = []      # Will hold the chosen coffee dictionaries
    len_coffe = len(COFFE_LIST)          # Total number of coffees on the menu
    print("What coffe do you want?: ")
    _print_coffe_list(len_coffe)         # Show the menu

    while True:
        # Get a valid selection number and adjust to list index (0-based)
        selected = COFFE_LIST[_get_number(len_coffe) - 1]

        if selected["available"]:        # Only process if the item is available
            # Ask how many cups and store the quantity inside the coffee dict itself
            selected["number_of_coffes"] = _how_namy_coffes(selected["name"])
            selected_coffes.append(selected)  # Add this coffee to the order
        else:
            print(f"Sorry the {selected['name']} is not available :c")

        # Ask if the customer wants to order another coffee
        if not _yes_or_not("Do you want order another coffe? (Y/n): "):
            return selected_coffes        # End the order process and return the list
        print("Select the next coffe please: ")  # Prompt for the next coffee


def get_total_price(order: list[dict]) -> int | float:
    """Calculate the total cost of the order using arithmetic and assignment operators."""
    total = 0                            # Initialize the running total to 0
    for coffe in order:                 # Loop through each coffee in the order
        # Multiply the unit price by the number of cups and add to the total
        # The '+=' is an assignment operator that adds the right-hand value to 'total'
        total += coffe["price"] * coffe["number_of_coffes"]
    return total


### This is Main! ###
def main() -> None:
    """Main program flow: greet customer, take order, calculate total, display result."""
    name = get_name()                     # Get the customer's name
    print(f"Welcome {name}")              # Greet them

    order = get_order()                   # Take the order
    total_price = get_total_price(order)  # Calculate the total cost

    # If nothing was ordered (total is 0), display a special message
    if total_price == 0:
        print(f"Custommer {name} didn't make an order.")

    # Build the output sentence with all ordered items
    print(f"Custommer {name} is buying ", end="")
    for coffe in order:
        # Print each item's quantity and name, followed by a comma
        print(f"{coffe["number_of_coffes"]} {coffe["name"]}(s), ", end="")
    # Complete the sentence with the total amount
    print(f"for a total amount of {total_price}$.")


### Calling Main ###
# This checks if the script is being run directly (not imported as a module).
# If so, it calls the main() function to start the program.
if __name__ == "__main__":
    main()
