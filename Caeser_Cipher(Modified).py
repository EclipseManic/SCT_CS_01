def encrypt(num, shift):
    result = ""
    for char in num:
        result += chr((((ord(char) - 32) + shift) % 95) + 32)
    return result
def decrypt(result, shift):
    return encrypt(result, -shift)
print("---------------------Enter Your Choice -------------------\n1. Encrypt\n2. Decrypt\n3. Exit \n--------------------------------------")
choice = input("Enter your choice :- ")
if choice == '1':
    num = input("Enter the Text u want to encrypt :-")
    shift = int(input("Enter the numeber of jump u want to (0-94) :-"))
    print("Encrypt :-", encrypt(num, shift))
elif choice == '2':
    result = input("Enter the string u want to decrypt :-")
    shift = int(input("Enter the numeber of jump u want to (0-94) :-"))
    print("Decrypt :-", decrypt(result, shift))
elif choice == '3':
    print("Thanks for using this program")
else:
    print("Invalid choice")
