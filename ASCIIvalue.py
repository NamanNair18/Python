print("Enter The String:", end="")
text = input()
textlength=len(text)
for char in text:
    ascii = ord(text)
    print(char,"\t", ascii)
