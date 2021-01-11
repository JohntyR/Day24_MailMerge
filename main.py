# TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt") as namefile:
    name_list = namefile.read().splitlines()

with open("./Input/Letters/starting_letter.docx") as letterTemplate:
    templateText = letterTemplate.read()

    for name in name_list:
        mergedText = templateText.replace("[name]", name)
        with open(
            f"./Output/ReadyToSend/letter_for_{name}.docx", mode="w"
        ) as mailMergedLetter:
            mailMergedLetter.write(mergedText)
