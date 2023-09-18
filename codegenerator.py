import random

def encodeValue():
    # Take message to be encoded
    message = input("Enter value to encode: ")
    encodeKey = random.randint(1, 10)
    # For each character in the value
    charArray = []
    for i in message:
        # Set the character to +1 
        charArray += chr(ord(i)+encodeKey)

    encodedMessage = ""
    for i in charArray:
        encodedMessage += i
    # output encoded value
    print("Your message encoded is: " + encodedMessage)
    print("Your decoding key is: " + str(encodeKey))
    optionMenu()

def decodeValue():
    # Take message to be decoded
    message = input("Enter the message you would like to decode: ")
    decodeKey = int(input("Enter encryption key: "))
    # For each character in the value
    charArray = []
    for i in message:
        # Reverses the character by the key 
        charArray += chr(ord(i)-decodeKey)

    decodedMessage = ""
    for i in charArray:
        decodedMessage += i
    print("Your message decoded is: " + decodedMessage)
    optionMenu()

def optionMenu():   
    option = input("Press 1 to encode, 2 to decode or 3 to quit: ")
    if option == "1":
        encodeValue()
    elif option == "2":
        decodeValue()
    elif option == "3":
        quit

# Startup functions
optionMenu()
