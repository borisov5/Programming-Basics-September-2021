favorite_book = input()
book = input()
books_checked = 0
while favorite_book != book:
    book = input()
    books_checked += 1
    if book == "No More Books":
        break
if favorite_book == book:
    print(f"You checked {books_checked} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {books_checked} books.")