# My Solution:
```py
print("".join(map(lambda x: x if x == " " or x == "!" else chr(((ord(x) - 65 + 13) % 26) + 65) if ord(x) < 97 else chr(((ord(x) - 97 + 13) % 26) + 97), list("Baez Knows!") )))
```
Breaking it down:
```py
print(
  "".join(
    map(
      lambda x:
        x if x == " " or x == "!" else chr(
          (
            (
              ord(x) - 65 + 13
            ) % 26
          ) + 65
        ) if ord(x) < 97 else chr(
          (
            (ord(x) - 97 + 13) % 26
          ) + 97
        ),
      list("Baez Knows!")
    )
  )
)
```

## The Process:
The string "Baez Knows!" is split into individual characters with list().
Every character is passed into a `lambda` function, which performs the following:
```py
def process(character):
  if x == " " or x == "!":
    return character # return it as-is without modification
  if ord(x) < 97: # uppercase letters
    return chr(((ord(x) - 65 + 13) % 26) + 65)
    # subtract 65 because capital letter "A" starts at `65`
    # add 13 because rot13
    # % 26 to prevent numbers higher than or greater than 26 (because 26 letters)
  else: # lowercase letters
    return chr(((ord(x) - 97 + 13) % 26) + 97)
    # same thing as above except lowercase letter "a" starts at 97
```
After mapping each character to a new character, the resulting list of characters are joined with `"".join(<list>)` and printed.

# BellRinger24

# bellRingerp6
Create a python program that implements Caesar Cipher and encodes the following String
This is allowed

![image](https://github.com/user-attachments/assets/681f1046-b040-4cf8-8e0c-320720ed38a7)

https://www.digitalocean.com/community/tutorials/python-ord-chr
Baez Knows!
