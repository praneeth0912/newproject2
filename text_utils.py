def reverse_text(text):
    return text[::-1]

def character_count(text):
    return len(text) 

def vowel_count(text):

    vowels = "aeiouAEIOU"

    count = 0

    for character in text:

        if character in vowels:
            count += 1

    return count