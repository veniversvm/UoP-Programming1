from time import sleep


book_titles =  ["The Alchemist", "1984", "Moby Dick", "Pride and Prejudice"]

def _processing(time: int) -> None:
    for x in range(time):
        print(".", end="")       
        sleep(1)
    print("")

def book_list_manager(book_to_remove: str) -> list[str]:
    print("Original list: ")
    print(book_titles)
    sleep(1)
    print("Appending books...")
    sleep(1)
    book_titles.append("El Quijote")
    book_titles.append("The Lord of the Rings")
    print(f"The title {book_to_remove} is damage, remove process..." )
    _processing(3)
    book_titles.remove(book_to_remove)
    print(f"Book {book_to_remove} has sussefuly remove")
    sleep(1)
    print("Ordering books")
    _processing(3)
    print("Books succefully order")
    book_titles.sort()
    return book_titles


def tuple_operation() -> None:
    tuple_list = ("John Doe", "B1023", "2025-10-15")
    print(f"Tuplet's len: {len(tuple_list)}")
    try:
        tuple_list[0] = "Juan Topo"  
    except Exception as e:
        print(e)

def packing_unpacking(title: str, author: str, year: int) -> None:
    book_info = title, author, year
    print(f" Varleble 'book_info' value: {book_info}")
    print(f"Type: {type(book_info)}")
    a, b, c = book_info
    print(f"Title: {a}, Author: {b}, Year {c}")

def indexing_and_slicing() -> None:
    borrowed_books = [23, 19, 31, 27, 22, 30, 25]
    week_2_to_5 = borrowed_books[1:6]
    print(week_2_to_5)
    borrowed_books[0] = 20
    print(borrowed_books)
    pass

def main() -> None:
    print("hello world!")
    # book_list = book_list_manager("1984")
    # print(book_list)
    # tuple_operation()
    # packing_unpacking("Harry Poter", "J.K.Rolling", 1987)
    indexing_and_slicing()

if __name__ == "__main__":
    main()
