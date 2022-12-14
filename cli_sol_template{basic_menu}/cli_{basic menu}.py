"""
Written by Benjamin Jack Cullen aka Holographic_Sol
"""
loop = True


def print_menu():
    global loop
    print(23 * "-", "Main Menu", 23 * "-")
    print("")
    print("1. Option 1")
    print("")
    print("")
    print("Press C for configuration menu")
    print("Press Q to quit                          Press H for help")
    print(62 * "-")
    choice = input("Select [1-?]: ")

    if choice == "q":
        loop = False

    elif choice == "c":
        print_config_menu()

    elif choice == "h":
        print_help()

    elif choice == "1":
        funk_1()

    else:
        print("-- invalid input:", choice)
        print_menu()


def print_config_menu():
    print(24 * "-", "Configuration Menu", 24 * "-")
    print("")
    print("1. Configuration 1")
    print("")
    print("")
    print("Press Q to quit configuration menu.")
    print("")

    selection = input("Select option: ")

    if selection == "q":
        print_menu()

    elif selection == "1":
        funk_conf_1()

    else:
        print("-- invalid input:", selection)
        print_config_menu()


def print_help():
    print(25 * "-", "Help", 25 * "-")
    print("")
    print("")
    print("")
    print("")
    print("Press Q to quit")
    print(62 * "-")
    choice = input("Select [1-?]: ")

    if choice == "q":
        print_menu()
    else:
        print("-- invalid input:", choice)
        print_menu()


def funk_conf_1():
    print('-- plugged in funk_conf_1')


def funk_1():
    print('-- plugged in funk_1')


while loop:
    print_menu()

