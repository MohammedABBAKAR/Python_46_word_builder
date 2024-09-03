# New Word Builder
# todo Create a function that builds a word from the scrambled letters contained in the first list. 
# todo Use the second list to establish each position of the letters in the first list.
# todo Return a string from the unscrambled letters (that made-up the word).

# * Examples
# ? word_builder(["g", "e", "o"], [1, 0, 2]) ➞ "ego"

# ? word_builder(["e", "t", "s", "t"], [3, 0, 2, 1]) ➞ "test"

# ? word_builder(["b", "e", "t", "i", "d", "a"], [1, 4, 5, 0, 3, 2]) ➞ "edabit"

# ! Notes

# * The elements in the second list are indexes of the elements in the first list.




# def word_builder(ltr, pos):
#     for item in pos:

liste1 = [1, 2, 3]
liste2 = ['a', 'b', 'c']
for element1, element2 in zip(liste1, liste2):
    print(element1, element2)

# nor = liste2[0]+liste2[1]+liste2[2]
# print(nor)


def word_builder(ltr, pos):
        tito = ""
        for item in pos:
           nor = ltr[item]
           tito += nor
        return tito
print(word_builder(["g", "e", "o"], [1, 0, 2]))
print(word_builder(["e", "t", "s", "t"], [3, 0, 2, 1]))



def word_builder(letters, positions):
    result = []
    for index in positions:
        result.append(letters[index])
    return ''.join(result)


print(word_builder(["g", "e", "o"], [1, 0, 2]))  
print(word_builder(["e", "t", "s", "t"], [3, 0, 2, 1]))  
print(word_builder(["b", "e", "t", "i", "d", "a"], [1, 4, 5, 0, 3, 2])) 
