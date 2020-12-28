import re


def naive_substring_search(string, pattern_string):
    occurrences = []

    for i in range(len(string) - len(pattern_string) + 1):
        for j in range(len(pattern_string)):
            if string[i + j] != pattern_string[j]:
                break
        else:
            occurrences.append(i)
    return occurrences


def read_data(path):
    with open(path, 'r') as f:
        string, pattern_string = tuple(map(str.strip, (path.readline(), path.readline())))
    return string, pattern_string


def algorithm(path):
    return naive_substring_search(read_data(path))


def re_algorightm(path):
    substring = read_data(path)[1]
    string = read_data(path)[0]
    ([match.span()[0] for match in tuple(re.finditer(substring, string))])
