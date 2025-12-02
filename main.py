message = "lapin"
key = 3

crypted_message = ""
for char in message:
    crypted_char = chr((ord(char) + 3 ) % 1_114_112)
    crypted_message += crypted_char
    print(crypted_message)