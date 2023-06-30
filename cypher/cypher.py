# Function to encrypt the message.
def encryption_function(encryption_result):
    for i in message:
        # Get the Unicode code of a letter.
        number = ord(i)
        if i == " ":
            count = 0
            count += 1
            encryption_result += i
        # Unicode capital letter range 65-90.
        elif 65 <= number <= 90:
            # Get character whose code matches Unicode.
            if number + key > 90:
                # If we go beyond the range of 65-90 subtract 26 (number of letters in the alphabet).
                encryption_result += chr(number + key - 26)
            else:
                encryption_result += chr(number + key)
        # Unicode lowercase letter range 97-122.        
        elif 97 <= number <= 122:
            # Get character whose code matches Unicode.
            if number + key > 122:
                # If we go beyond the range of 97-122 subtract 26 (number of letters in the alphabet).
                encryption_result += chr(number + key - 26)
            else:
                encryption_result += chr(number + key)
        else:
            # Other characters and space are added to the variable.
            encryption_result += i
    return (encryption_result)

message = input("\nEnter your message: ")
# Shift 15 letters to the right.
key = 15
# Put the encryption result in this variable.
encryption_result = ""

# Calling a function and storing the encrypted message in a variable.
encrypted_message = encryption_function(encryption_result)

# Printing the encoded message.
print(f"\nCipher of your message: {encrypted_message}\n")