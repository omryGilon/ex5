

def check_words_in_st_permutations(words_set, st, count_table):

    # Each inner iteration cuts the word into a small portion of it, and checks if it belongs to
    # the words_set
    # Since not specified otherwise, words of length zero are checked as well.
    for i in range(len(st)):
        for j in range(i+1, len(st)+1):
            mini_word = st[i:j]

            if mini_word in words_set:
                if mini_word in count_table:
                    count_table[mini_word] += 1
                else:
                    # creating a new value in the dictionary
                    count_table.update({mini_word: 1})


def check_words_in_matrix_strings(words_set, strings_in_matrix):
    """
    Gets a set of words (dog, cat etc...) and a list of string in the matrix (["abfjdog", "catbbb"]).
    The method will find the number of times each word appears in the provided strings of the matrix.
    The function will return a dictionary in which each word has the number of times it appears in the strings.
    A word that has 0 occurrences would not be in the dictionary.
    """
    count_table = {}
    for st in strings_in_matrix:
        check_words_in_st_permutations(words_set, st, count_table)

    return count_table
