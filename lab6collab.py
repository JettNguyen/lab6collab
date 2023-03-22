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

        if int(char) + 3 > 10:                  # Diego: added to check if the sum is over 10

            encoded += str((int(char)+3) % 10)  # Diego: added to take only the last digit if the sum is over 10
                                                # example if 9 input 9 + 3 = 12 take only 2
        else:

            encoded += (str(int(char) + 3))  # adds 3 to each number in the password

    return encoded


def decode(password_encoded):

    password_decoded_list = []

    for i in range(0, len(password_encoded)):
        password_decoded_list.append(int(password_encoded[i]) - 3)

        if password_decoded_list[i] < 0:
            password_decoded_list[i] = password_decoded_list[i] + 10

    password_decoded = ''

    for j in range(0, len(password_decoded_list)):
        password_decoded += str(password_decoded_list[j])

    return password_decoded


if __name__ == "__main__":
    main()
