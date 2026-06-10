def display():
    f = open("contacts.txt", "r")
    print(f.read())
    f.close()


def search():
    name = input("Enter name: ")

    f = open("contacts.txt", "r")
    for line in f:
        if line.lower().startswith(name.lower() + ","):
            print(line.strip())
            break
    else:
        print("Contact not found")

    f.close()


def add():
    name = input("Enter name: ")
    number = input("Enter number: ")

    f = open("contacts.txt", "a")
    f.write(f"\n{name},{number}")
    f.close()

    print("Contact added")


def update():
    name = input("Enter name to update: ")

    f = open("contacts.txt", "r")
    data = f.readlines()
    f.close()

    f = open("contacts.txt", "w")

    for line in data:
        n, num = line.strip().split(",")

        if n.lower() == name.lower():
            num = input("Enter new number: ")
            print("Contact updated")

        f.write(f"{n},{num}\n")

    f.close()


def delete():
    name = input("Enter name to delete: ")

    f = open("contacts.txt", "r")
    data = f.readlines()
    f.close()

    f = open("contacts.txt", "w")

    for line in data:
        n, num = line.strip().split(",")

        if n.lower() != name.lower():
            f.write(line)
        else:
            print("Contact deleted")

    f.close()


def vowel_contacts():
    f = open("contacts.txt", "r")

    print("Contacts starting with vowels:")
    for line in f:
        n, num = line.strip().split(",")

        if n[0].lower() in "aeiou":
            print(n, num)

    f.close()


# Main Program
while True:
    print("\n1. Display Contacts")
    print("2. Search Contact")
    print("3. Add Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Contacts Starting with Vowels")
    print("7. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        display()

    elif ch == 2:
        search()

    elif ch == 3:
        add()

    elif ch == 4:
        update()

    elif ch == 5:
        delete()

    elif ch == 6:
        vowel_contacts()

    elif ch == 7:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")