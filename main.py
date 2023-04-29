import ciphar_code as ciphar
import art

print (art.logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    ciphar.encrypt(plain_text=text, shift_number=shift)

elif direction == "decode":
    ciphar.decrypt(ciphar_text=text, shift_number=shift)

else:
    print ("***Please enter either 'encode' or 'decode'.***")
