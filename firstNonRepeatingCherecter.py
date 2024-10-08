string = input()
repeating_characters = ''
non_repeating_characters = ''

for i in string:
    for j in string:
        if j==i:
            repeating_characters+=j 

for i in repeating_characters:
    for j in repeating_characters:
        if j!=i:
            non_repeating_characters+=j 

print(non_repeating_characters[0])