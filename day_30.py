import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(new_dict)


def word_in():
    word = input("Enter a word: ").upper()
    try:
        output_list = [new_dict[letter] for letter in word]
    except KeyError:
        print("Вводите только буквы")
        word_in()
    else:
        print(output_list)

word_in()