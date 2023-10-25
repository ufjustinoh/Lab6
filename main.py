# Leah Jones and Justin Oh
# Function for the menu display
def menu_display():
    print("\nMenu")
    print("-" * 13)

    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(password):
    encoded_string = ""
    for digit in password:
        if digit == "7":
            encoded_string += "0"
        elif digit == "8":
            encoded_string += "1"
        elif digit == "9":
            encoded_string += "2"
        encoded_string += str(int(digit) + 3)
    return encoded_string


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
