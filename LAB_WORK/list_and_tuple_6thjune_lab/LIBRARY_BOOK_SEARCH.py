# List of books (Book Name, Number of Copies)
books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

# Display unavailable books
print("Unavailable Books:")
for book in books:
    if book[1] == 0:
        print(book[0])

# Find all books with more than 2 copies
print("\nBooks with more than 2 copies:")
for book in books:
    if book[1] > 2:
        print(book[0], "-", book[1], "copies")

# Count available books
count = 0

for book in books:
    if book[1] > 0:
        count += 1

print("\nNumber of available books:", count)

# Stop searching once a requested book is found
search_book = input("\nEnter book name to search: ")

for book in books:
    if book[0].lower() == search_book.lower():
        print("Book Found!")
        print("Title:", book[0])
        print("Copies Available:", book[1])
        break
else:
    print("Book not found")