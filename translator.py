


def translator(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou" :
            if letter.upper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translator(input("Enter the phrase : ")))    
        
        
        









