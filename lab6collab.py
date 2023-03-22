# Jett Nguyen
def main():
    program = True
    while program:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")  # main menu prints
        option = input("Please enter an option: ")  # takes the input of the user to determine what to execute
        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!\n")
        if option == "2":
            print("The encoded password is", encode(password), "and the original password is", decode(encoded),
                  end='.\n\n')
        if option == "3":
            program = False


def encode(password):
    encoded = ''
    for char in password:
        encoded += (str(int(char) + 3))  # adds 3 to each number in the password
    return encoded


if __name__ == "__main__":
    main()
