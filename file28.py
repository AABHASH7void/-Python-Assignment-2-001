ch = input("Enter a character: ").lower()

if ch.isalpha() and len(ch) == 1:
    if ch in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Please enter a single alphabet")