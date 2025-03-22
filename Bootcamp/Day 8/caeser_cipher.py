alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ]

alphabet_length = len(alphabet)
end_of_alphabet = alphabet_length - 1


def encrypt_message(text, shift):
    encrypted_message = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            shifted_position = position + shift
            if shifted_position > end_of_alphabet:
                offset_position = shifted_position - end_of_alphabet
                encrypted_message += alphabet[offset_position - 1]
            else:
                encrypted_message += alphabet[shifted_position]
        else:
            encrypted_message += letter
    print(encrypted_message)


def decrypt_message(text, shift):
    decrypted_message = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            shifted_position = position - shift
            decrypted_message += alphabet[shifted_position]
        else:
            decrypted_message += letter
    print(decrypted_message)


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt_message(text=text, shift=shift)
elif direction == "decode":
    decrypt_message(text=text, shift=shift)


