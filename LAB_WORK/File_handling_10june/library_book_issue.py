#program to manage library book issue system
def display():
    f = open("books.txt", "r")
    print(f.read())
    f.close()


def search():
    bid = input("Enter Book ID: ")

    f = open("books.txt", "r")
    for line in f:
        if line.startswith(bid):
            print(line.strip())
            break
    else:
        print("Book not found")

    f.close()


def issue():
    bid = input("Enter Book ID: ")

    f = open("books.txt", "r")
    data = f.readlines()
    f.close()

    f = open("books.txt", "w")

    for line in data:
        b_id, title, qty = line.strip().split(",")
        qty = int(qty)

        if b_id == bid:
            if qty > 0:
                qty -= 1
                print("Book Issued")
            else:
                print("Book Unavailable")

        f.write(f"{b_id},{title},{qty}\n")

    f.close()


def return_book():
    bid = input("Enter Book ID: ")

    f = open("books.txt", "r")
    data = f.readlines()
    f.close()

    f = open("books.txt", "w")

    for line in data:
        b_id, title, qty = line.strip().split(",")
        qty = int(qty)

        if b_id == bid:
            qty += 1
            print("Book Returned")

        f.write(f"{b_id},{title},{qty}\n")

    f.close()


def unavailable():
    f = open("books.txt", "r")

    print("Unavailable Books:")
    for line in f:
        b_id, title, qty = line.strip().split(",")

        if int(qty) == 0:
            print(b_id, title)

    f.close()


def restock():
    f = open("books.txt", "r")

    print("Books requiring restocking:")
    for line in f:
        b_id, title, qty = line.strip().split(",")

        if int(qty) < 2:
            print(b_id, title, qty)

    f.close()


# Main Program
while True:
    print("\n1.Display Books")
    print("2.Search Book")
    print("3.Issue Book")
    print("4.Return Book")
    print("5.Unavailable Books")
    print("6.Restocking Required")
    print("7.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        display()

    elif ch == 2:
        search()

    elif ch == 3:
        issue()

    elif ch == 4:
        return_book()

    elif ch == 5:
        unavailable()

    elif ch == 6:
        restock()

    elif ch == 7:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")