print("".join(map(lambda x: x if x == " " or x == "!" else chr(((ord(x) - 65 + 13) % 26) + 65) if ord(x) < 97 else chr(((ord(x) - 97 + 13) % 26) + 97), list("Baez Knows!") )))
