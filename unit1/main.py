### General coffe list ###
COFFE_LIST: list[dict] = [
    {
        "name": "Capuccino",
        "price": 3.50,
        "avaible": True,
    },
    {
        "name": "American",
        "price": 1,
        "avaible": True,
    },
    {
        "name": "Machiato",
        "price": 2.15,
        "avaible": False,
    },
]


### Inner functions ###
def _print_coffe_list(len_coffe: int) -> None:
    for i in range(len_coffe):
        print(f"{i+1} - {COFFE_LIST[i]["name"]} --- Price: {COFFE_LIST[i]["price"]}$")
    print(" ")


def _get_number(limit: int) -> int:
    while True:
        n = input()
        try:
            n = int(n)
            if n < 0 or n > limit:
                print("Please use a valid option.")
            else:
                return n
        except ValueError:
            print(f"Please use only numbers from 1 to {limit}.")


def _yes_or_not(msg: str) -> bool:
    if isinstance(msg, str):
        print(msg)
    else:
        print("Yes (y) or No (n): ")
    r = input()
    return r.lower() in ["yes", "y"]


def _how_namy_coffes(coffe_name: str = "coffe") -> int:
    print(f"How many {coffe_name}s do you want?: ")
    return _get_number(100)


### External Function ###
def get_name() -> str:
    print("Welcome to Marvelous Cafe\nCan give me your name?: ")
    while True:
        name: str = input()
        if isinstance(name, str) and name.strip().isalpha():
            return name
        else:
            print("Invalid name, you can only use 'letters' in name: ")


def get_order() -> list[dict]:
    selected_coffes: list[dict] = []
    len_coffe = len(COFFE_LIST)
    print("What coffe do you want?: ")
    _print_coffe_list(len_coffe)
    while True:
        selected = COFFE_LIST[_get_number(len_coffe) - 1]
        if selected["avaible"]:
            selected["number_of_coffes"] = _how_namy_coffes(selected["name"])
            selected_coffes.append(selected)
        else:
            print(f"Sorry the {selected['name']} is not avaible :c")
        if not _yes_or_not("Do you want order another coffe? (Y/n): "):
            return selected_coffes
        print("Select the next coffe please: ")


def get_total_price(order: list[dict]) -> int | float:
    total = 0
    for coffe in order:
        total += coffe["price"] * coffe["number_of_coffes"]
    return total


### This is Main! ###
def main() -> None:
    name = get_name()
    print(f"Welcome {name}")
    order = get_order()
    total_price = get_total_price(order)
    if total_price == 0:
        print(f"Custommer {name} didn't make an order.")
    print(f"Custommer {name} is buying ", end="")
    for coffe in order:
        print(f"{coffe["number_of_coffes"]} {coffe["name"]}(s), ", end="")
    print(f"for a total amount of {total_price}$.")


### Calling Main ###
if __name__ == "__main__":
    main()
