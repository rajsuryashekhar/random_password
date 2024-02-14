import random
import string


letters = string.ascii_letters
digit = string.digits
symbols = string.punctuation

print("-"*120)
length = int(input("Enter the desired length of Password : "))
difficulty = int(
    input("Select password difficulty : \n  1) Low \n  2) Medium \n  3) Deficult \n\n  Select (1/2/3) : ")
    )

if difficulty == 1:
    characters_set = letters
elif difficulty == 2:
    characters_set = letters + digit
elif difficulty == 3:
    characters_set = letters + digit + symbols
else:
    characters_set = letters + digit
    print("Wromg selection!, Default selected is Medium.")


password = "".join(random.choices(characters_set,k= length))
print("-"*120)
print("Password Generated  : "+password)
print("-"*120)