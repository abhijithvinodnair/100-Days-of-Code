individual_names = []
update_names = ""

with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
    letter_words = letter.read()
with open("./Input/Names/invited_names.txt") as Names:
    letter_names = Names.read()
for i in letter_names:
    if i!= '\n':
        update_names += i
    else:
        individual_names .append(update_names)
        update_names = ""
for names in individual_names:
    new_letter = letter_words.replace("[Name]", f"{names}")
    tobesend =  open(f"./Output/{names}.txt",mode ="w")
    tobesend.write(f"{new_letter}")
    tobesend.close()

