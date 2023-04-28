alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

''' Code for Encrytion starts '''

def encrypt(plain_text, shift_number):
    ciphar_text = ''
    for char in plain_text:
        #modulus with 26 ensures that the shifted_index does not go out of range
        shifted_index = (alphabet.index(char) + shift_number) % 26
        ciphar_text += alphabet[shifted_index] 
        
    print (f"The encoded text is {ciphar_text}")


''' Code for Decrytion starts '''

def decrypt(ciphar_text, shift_number):
    plain_text = ''
    for char in ciphar_text:
      shifted_index = (alphabet.index(char) - shift_number) % 26
      plain_text += alphabet[shifted_index] 
        
    print (f"The decoded text is {plain_text}")