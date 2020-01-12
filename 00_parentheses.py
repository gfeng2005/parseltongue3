iles = input()

def alternate_case(iles):
    hi = iles[::2].upper()
    lo = iles[1::2].lower()
    return ''.join([u+v for u, v in zip(hi, lo)])

print(alternate_case(iles))
aux = [(alternate_case(iles))]

def asterisk_vowel(aux):
    vowels = 'aeiouAEIOU'
    for words in aux:
        for char in words:
            if char.lower() in vowels:
                words = words.replace(char, '*')
            if char.upper() in vowels:
                words = words.replace(char, '*')
            return words

print(asterisk_vowel(aux))

def check_parentheses(aux):
    paren = '()'
    even = '2, 4, 6, 8, 10'
    if count(paren) in aux == even:
        print("Balanced? Yes.")
    else:
        print("Balanced? No.")
