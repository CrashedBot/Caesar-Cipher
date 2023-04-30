import ciphar_code as ciphar
import art

print (art.logo)

should_continue = True

while should_continue == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: (Only for Strings)\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        ciphar.encrypt(plain_text=text, shift_number=shift)

    elif direction == "decode":
        ciphar.decrypt(ciphar_text=text, shift_number=shift)

    else:
        print ("***Please enter either 'encode' or 'decode'.***")


    rerun = input("Do you want to rerun the program? (Yes/No) ").lower()

    if rerun == "yes":
        should_continue = True
    elif rerun == "no":
        print ("GoodBye.")
        should_continue = False
    else:
        print ("Invaild Input. ")
