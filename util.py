import re


def naive_substring_search(string, pattern_string):
    concurrences = []
    for i in range(len(string) - len(pattern_string) + 1):
        for j in range(len(pattern_string)):
            if string[i + j] != pattern_string[j]:
                break
        else:
            concurrences.append(i)
    return concurrences


def read_data(path):
    with open(path, 'r') as f:
        string, pattern_string = tuple(map(str.strip, (f.readline(), f.readline())))
    return string, pattern_string


def algorithm(path):
    data = read_data(path)
    return naive_substring_search(data[0], data[1])


def re_substings(path):
    substring = read_data(path)[1]
    string = read_data(path)[0]
    return [match.start() for match in tuple(re.finditer(substring, string))]

