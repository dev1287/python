#name = 'raghavendra'
#print(name)


text = input("Enter any string:")
shift = int(input("Enter shift: "))
new_text = "".join([chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97) if char.islower() else char for char in text])
print("cipher text:", new_text)
