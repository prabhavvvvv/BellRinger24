text  ="Hi"
message = ""
for char in text:
    if char.isalpha():
        upper = ord("A")
    elif char.isupper():
        lower = ord("a")
print(message)
