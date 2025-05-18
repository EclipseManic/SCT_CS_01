def encrypt(num,shift): #This function encrypts the text using Caesar cipher
    global result #This variable is used to store the encrypted text
    result = ""#This variable is used to store the encrypted text
    for char in num:#This loop iterates through each character in the input text
        if char.isupper():#This condition checks if the character is uppercase
         base = ord('A') #This variable is used to store the ASCII value of 'A'
         result += chr((ord(char) - base + shift) % 26 + base )#This line encrypts the character by shifting it by the specified number of positions and stores the encrypted character in the result variable
        elif char.islower(): #This condition checks if the character is lowercase
            base = ord('a')
            result += chr((ord(char) - base + shift) % 26 + base )
        else :#This condition checks if the character is neither uppercase nor lowercase
            result+=char #This line adds the character to the result variable without any changes
    return result
def decrypt(result,shift): #This function decrypts the text using Caesar cipher
    print("Decrypt :- ",encrypt(result,-shift))#This line calls the encrypt function with a negative shift value to decrypt the text and prints the decrypted text
print("---------------------Enter Your Choice -------------------\n1. Encrypt\n2. Decrypt\n3. Exit \n--------------------------------------")   
choice = (input("Enter your choice :- "))#This line prompts the user to enter their choice
if choice == '1' :#This condition checks if the user wants to encrypt the text
    num = input("Enter the Text u want to encrypt :- ")
    shift = int(input("Enter the numeber of jump u want to (0-25) :-"))
    print("Encrypt :- ",encrypt(num,shift))
elif choice == '2':#This condition checks if the user wants to decrypt the text
    result = input("Enter the string u want to decrypt :- ")
    shift = int(input("Enter the numeber of jump u want to (0-25) :-"))
    decrypt(result,shift)
elif choice == '3':
    print("Thanks for using this program")
elif choice is not '1' or '2' or '3' :#This condition checks if the user has entered an invalid choice
    print("Invalid choice")
