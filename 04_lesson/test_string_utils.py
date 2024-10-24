import pytest
from string_utils import StringUtils

string = StringUtils()

# Проверка capitilize
@pytest.mark.parametrize("str1, result",
                         [
                             ("stroka", "Stroka"),
                             ("stroka iz neskolkih slov", "Stroka iz neskolkih slov"),
                             ("русский язык", "Русский язык"),
                             ("Text", "Text")
                         ])
def test_string_capitilize_positive(str1, result):
    assert string.capitilize(str1) == result

@pytest.mark.parametrize("str2, result",
                         [
                             (" ", " "),
                             (" 1", " 1"),
                             ("", ""),
                             ("951595", "951595"),
                             ("!@#$%^&*()", "!@#$%^&*()")
                          ])
def test_string_capitilize_neg(str2, result):
    assert string.capitilize(str2) == result

@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize("str2, result",
                         [
                             (" text", " Text"), # при Text - ошибка
                             ("  multiple   spaces", "  Multiple   spaces") # при Multiple   spaces - ошибка
                          ])
def test_string_capitilize_neg(str2, result):
    assert string.capitilize(str2) == result

# Проверка trim
@pytest.mark.parametrize("str3, result",
                         [
                             (" stroka", "stroka"),
                             (" stroka iz neskolkih slov", "stroka iz neskolkih slov"),
                             ("  strings strings", "strings strings"),
                             ("      123 ", "123 "),
                             (" !@#$$%%^&", "!@#$$%%^&")
                         ])
def test_string_trim_positive(str3, result):
    assert string.trim(str3) == result

@pytest.mark.parametrize("str4, result",
                         [
                             ("stroka", "stroka"),
                             ("strings strings", "strings strings"),
                             ("123 ", "123 "),
                             ("!@#$$%%^&", "!@#$$%%^&")
                         ])
def test_string_trim_neg(str4, result):
    assert string.trim(str4) == result

# Проверка to_list
@pytest.mark.parametrize('str5, delimeter, result',
                         [
                             ('t:e:x:t', ':', ['t', 'e', 'x', 't']),
                             (' 1 2 3 ', ' ', ['', '1', '2', '3', '']),
                             ('t,e,x,t', ',', ['t', 'e', 'x', 't']),
                             ('1 lesson,2 lesson', ',', ['1 lesson', '2 lesson']),
                         ])
def test_string_to_list_positive(str5, delimeter, result):
    assert string.to_list(str5, delimeter) == result

@pytest.mark.parametrize('str6, delimeter, result',
                         [
                             ('', '', []),
                             (' ', ' ', []),
                             (':', ':', ['',''])
                         ])
def test_string_to_list_neg(str6, delimeter, result):
    assert string.to_list(str6, delimeter) == result
    # сверка результатов
    # print(repr(string.to_list(str6, delimeter)))
    # print(repr(result))

# Проверка contains
@pytest.mark.parametrize('str7, symbol, res',
                         [
                             ('Vika', 'V', True),
                             ('Vika Isaeva', ' ', True),
                             ('Vika Isaeva','a', True),
                             ('Vika Isaeva','u', False)
                         ])
def test_string_contains_positive(str7, symbol, res):
    assert string.contains(str7, symbol) == res

@pytest.mark.parametrize('str8, symbol, res',
                         [
                             ('', 'V', False),
                             (' ', 'i', False),
                             ('@#$%^&','*', False)
                         ])
def test_string_contains_neg(str8, symbol, res):
    assert string.contains(str8, symbol) == res

# Проверка delete_symbol
@pytest.mark.parametrize('str9, symbol, res1',
                         [
                             ("SkyPro", "k", "SyPro"),
                             ("Viktoria Isaeva", "tori", "Vika Isaeva"),
                             ("SkyPro Skyeng Skybidy", "Sky", "Pro eng bidy"),
                             (" S k y P r o ", " ", "SkyPro")
                         ])
def test_string_delete_symbol_positive(str9, symbol, res1):
    assert string.delete_symbol(str9, symbol) == res1

@pytest.mark.parametrize('str10, symbol, res1',
                         [
                             ("SkyPro", " ", "SkyPro"),
                             ("1 and 1", "", "1 and 1"),
                             ("SkyPro", "T", "SkyPro"),
                             ("Sky Pro", "  ", "Sky Pro")
                         ])
def test_string_delete_symbol_neg(str10, symbol, res1):
    assert string.delete_symbol(str10, symbol) == res1

# Проверка starts_with
@pytest.mark.parametrize('str11, symbol, res',
                         [
                             ('Vika', 'V', True),
                             ('vika Isaeva', 'v', True),
                             (' Vika Isaeva',' ', True),
                             ('1Vika Isaeva','1', True),
                             ('', '', True)
                         ])
def test_string_starts_with_positive(str11, symbol, res):
    assert string.starts_with(str11, symbol) == res

@pytest.mark.parametrize('str12, symbol, res',
                         [
                             ('Vika', 'v', False),
                             ('vika Isaeva', 'V', False),
                             (' Vika Isaeva', 'V', False),
                             ('Vika Isaeva', 'I', False),
                             ('', ' ', False)
                         ])
def test_string_starts_with_neg(str12, symbol, res):
    assert string.starts_with(str12, symbol) == res

# Проверка end_with
@pytest.mark.parametrize('str13, symbol, res',
                         [
                             ('Vika', 'a', True),
                             ('vika I', 'I', True),
                             ('Vika Isaeva ',' ', True),
                             ('Vika Isaeva1','1', True),
                             ('', '', True)
                         ])
def test_string_end_with_positive(str13, symbol, res):
    assert string.end_with(str13, symbol) == res

@pytest.mark.parametrize('str14, symbol, res',
                         [
                             ('Vika', 'v', False),
                             ('vika Isaeva', 'A', False),
                             (' Vika Isaeva', '', False),
                             ('Vika Isaeva  .', ' ', False),
                             ('', ' ', False)
                         ])
def test_string_end_with_neg(str14, symbol, res):
    assert string.end_with(str14, symbol) == res

@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize('str14, symbol, res',
                         [
                             (' Vika Isaeva', '', False) # сравнение строки с пустым значением  - ошибка
                         ])
def test_string_end_with_neg(str14, symbol, res):
    assert string.end_with(str14, symbol) == res

# Проверка is_empty
@pytest.mark.parametrize('str15, res',
                         [
                             ('   ', True),
                             (' ', True),
                             ('', True)
                         ])
def test_string_is_empty_positive(str15, res):
    assert string.is_empty(str15) == res


@pytest.mark.parametrize('str16, res',
                         [
                             ('Vika',  False),
                             ('vika Isaeva',  False),
                             (' Vika Isaeva ', False)
                         ])
def test_string_is_empty_neg(str16, res):
    assert string.is_empty(str16) == res

# Проверка list_to_string
@pytest.mark.parametrize('lst, joiner, result',
                         [
                             (["t","e","x","t"], ",", "t,e,x,t"),
                             ([1, 2, 3], " ", "1 2 3"),
                             (["apple", "pear", "plum", "apricot"], "-", "apple-pear-plum-apricot"),
                             (["1 lesson", "2 lesson"], "/", "1 lesson/2 lesson")
                         ])
def test_string_list_to_string_positive(lst, joiner, result):
    assert string.list_to_string(lst, joiner) == result

@pytest.mark.parametrize('lst, joiner, result',
                         [
                             (["", "e"], ",", ",e"),
                             ([" ", "e"], ",", " ,e"),
                             ([], ",", ""),
                             ([(),()], "/", "()/()"),
                         ])
def test_string_list_to_string_neg(lst, joiner, result):
    assert string.list_to_string(lst, joiner) == result
    # сверка результатов
    # print(repr(string.list_to_string(lst, joiner)))
    # print(repr(result))
