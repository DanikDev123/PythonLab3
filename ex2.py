table = int(input("Enter an Ascii value: "))
if table < 0 or table > 127:
    print("Invalid input")
print (f"The character is: {chr(table)}")
