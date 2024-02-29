import pandas


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output = [alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output)


data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}
generate_phonetic()