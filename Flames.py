'''
Simple Flames game using python
'''

name1 = input("Enter the name of the first person: ").replace(" ", "").lower()
name2 = input("Enter the name of the second person: ").replace(" ", "").lower()

flames = "flames"

for letter in name1[:]:
    if letter in name2:
        name1 = name1.replace(letter, "", 1)
        name2 = name2.replace(letter, "", 1)

name = name1 + name2
name_length = len(name)

while len(flames) > 1:
    split = (name_length % len(flames)) - 1

    if split >= 0:
        flames = flames[split + 1:] + flames[:split]
    else:
        flames = flames[:-1]

result_mapping = {
    "f": "Friendship",
    "l": "Love",
    "a": "Affection",
    "m": "Marriage",
    "e": "Enmity",
    "s": "Sisterhood"
}

print("Result:", result_mapping.get(flames, "Error"))