# Leah Jones and Justin Oh
# Function for the menu display
def menu_display():
    print("\nMenu")
    print("-" * 13)

    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


# Have user input their password to be decoded in a loop
def main():
    while True:
        menu_display()

        user_opt = input("\nPlease enter an option: ")

        if user_opt == "1":
            my_pass = input("Please enter your password to encode: ")
            encoded_pass = encode(my_pass)
            print("Your password has been encoded and stored!")
        elif user_opt == "2":
            print("The encoded password is " + encoded_pass + " and the original password is " + my_pass)
        elif user_opt == '3':
            break


if __name__ == '__main__':
    main()
