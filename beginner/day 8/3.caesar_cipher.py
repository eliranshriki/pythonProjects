from logo_caesar_cipher import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def caesar(diraction, plain_text, shift_amount):
    code_text = ""
    decode_text = ""
    if direction == "encode":
        for letter in plain_text:
            if letter not in alphabet:
                code_text += letter
            else:
                position = alphabet.index(letter)
                new_position = position + shift_amount % 26
                code_text += alphabet[new_position]
        print(f"The encoded text is {code_text}")
    elif direction == "decode":
        for letter in plain_text:
            if letter not in alphabet:
                decode_text += letter
            else:
                position = alphabet.index(letter)
                new_position = position - shift_amount % 26
                decode_text += alphabet[new_position]
        print(f"The decoded text is {decode_text}")
    else:
        print("I Don't Know What You Wand To Do!!!!")

should_continue=True
while should_continue == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(diraction=direction, plain_text=text, shift_amount=shift)
  result=input("Type 'yes' if you want to continue or 'no' if you want to stop\n")
  if result == "no":
    should_continue=False
    print ("good bay")
