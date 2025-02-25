# TASK: Create an interactive grocery list manager.

def append(item: str) -> list:
    """Adds an item to list 'groceries' """
    item = item.strip().title()
    grocery_list.append(item)
    grocery_list.sort()
    print(f"Item '{item}' added to list")

def remove(item: str) -> list:
    """Removes an item from list 'grocery_list' """
    item = item.strip().title()
    if item in grocery_list:
        grocery_list.remove(item)
        grocery_list.sort()
        print(f"Item '{item}' removed to list")
    else: 
        print("Item not in list. ")

def display_list():
    """Lets the user see list 'grocery_list' """
    if grocery_list:
        print("Your list: ")
        for index, item in enumerate(grocery_list, start=1):
            print(f"{index}. {item}")
    else: 
        print("No items in list. ")


grocery_list = []

while True:
    try: 
        choice = int(input("What would you like to do?  [1] Add item to list , [2] Remove item from list, [3] View list, [4] Exit. "))
        if choice == 1:
            add = input("What would you like to add to the list? ")
            append(add)

        elif choice == 2:
            delete = input("What would you like to remove from the list? ")
            remove(delete)

        elif choice == 3: 
            display_list()

        elif choice == 4:
            exit()
        
        else:
            print("Invalid input")

    except ValueError:
        print("Invalid input")