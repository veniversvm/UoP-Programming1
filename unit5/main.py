from time import sleep

# Global list representing available books in the library
book_titles = ["The Alchemist", "1984", "Moby Dick", "Pride and Prejudice"]


def _processing(seconds: int) -> None:
    """Helper function to simulate a visually interactive processing delay."""
    for _ in range(seconds):
        print(".", end="", flush=True)
        sleep(1)
    print("")


def book_list_manager(book_to_remove: str) -> list[str]:
    """Demonstrates list mutation: adding, removing, and sorting book titles."""
    print("Original list:")
    print(book_titles)
    sleep(1)

    print("\nAppending new books to the library...")
    sleep(1)
    book_titles.append("Don Quijote")
    book_titles.append("The Lord of the Rings")

    print(f"The book '{book_to_remove}' is damaged. Initiating removal process...")
    _processing(3)
    book_titles.remove(book_to_remove)
    print(f"Book '{book_to_remove}' has been successfully removed.")
    sleep(1)

    print("\nSorting book list alphabetically...")
    _processing(3)
    book_titles.sort()
    print("Books successfully sorted.")

    return book_titles


def tuple_operation() -> None:
    """Demonstrates tuple immutability and iteration over tuple elements."""
    borrower_info = ("John Doe", "B1023", "2025-10-15")
    print(f"Borrower record length: {len(borrower_info)} fields.")

    print("\nIterating through tuple elements:")
    for field in borrower_info:
        print(f" - Field data: {field}")

    print("\nAttempting to modify an element in the immutable tuple...")
    try:
        # Intentionally raising a TypeError to demonstrate immutability
        borrower_info[0] = "Hans Moleman"
    except TypeError as e:
        print(f"Observation / Error caught: {e}")


def packing_unpacking(title: str, author: str, year: int) -> None:
    """Demonstrates packing discrete variables into a tuple and unpacking them."""
    print("Packing book details into a single tuple structure...")
    book_info = title, author, year
    sleep(1)

    print(f"Variable 'book_info' value: {book_info}")
    print(f"Data type: {type(book_info)}")

    print("Sending trough internet")
    _processing()

    print("Packet recieve")
    sleep(1)
    print("\nUnpacking tuple into separate variables...")
    sleep(1)
    unpacked_title, unpacked_author, unpacked_year = book_info
    print(f"Title: {unpacked_title}")
    print(f"Author: {unpacked_author}")
    print(f"Publication Year: {unpacked_year}")


def indexing_and_slicing() -> None:
    """Demonstrates sequence slicing and element modification using list indexing."""
    borrowed_books = [23, 19, 31, 27, 22, 30, 25]
    print(f"Original weekly statistics: {borrowed_books}")

    # Slicing from Week 2 (index 1) through Week 5 (index 4 inclusive -> stop index 5)
    week_2_to_5 = borrowed_books[1:5]
    sleep(1)
    print(f"Extracted records (Week 2 to Week 5): {week_2_to_5}")

    sleep(1)
    print("\nUpdating Week 1 record via indexing...")
    borrowed_books[0] = 20
    sleep(1)
    print(f"Updated weekly statistics list: {borrowed_books}")


def main() -> None:
    """Main execution entry point demonstrating each task sequentially."""
    print("=== LIBRARY MANAGEMENT SYSTEM LOGS ===\n")

    print("--- Question 1: List Operations ---")
    final_list = book_list_manager("1984")
    print(f"Final Inventory: {final_list}\n")

    print("--- Question 2: Tuple Immutability ---")
    tuple_operation()

    print("\n--- Question 3: Tuple Packing and Unpacking ---")
    packing_unpacking("Harry Potter", "J.K. Rowling", 1997)

    print("\n--- Question 4: Indexing and Slicing ---")
    indexing_and_slicing()


if __name__ == "__main__":
    main()