import pytest
import ex5


@pytest.mark.parametrize("words_set, matrix_strings, expected", [
    ({"dog"}, ["dog", "dogdog"], {"dog": 3}),
    ({"dog"}, ["do", "og", "", "dg"], {}),
    ({"dog"}, ["cat", "fish"], {}),
    ({"dog", "cat"}, ["dogcat", "catdog"], {"dog": 2, "cat":2}),
    ({"d"}, ["dog", "dogdogd"], {"d": 4}),
    ({""}, ["dog", "dogdog"], {},),
    ({"app", "appl"}, ["appleapple"], {"appl":2, "app":2},),

])
def test_check_words_in_matrix_strings(words_set, matrix_strings, expected):
    assert ex5.check_words_in_matrix_strings(words_set, matrix_strings) == expected

