# torob interview
from multiprocessing import Pool
import heapq
from collections import defaultdict

special_chars = ['"', '(', ')', '{', '}', '[', ']', '.', "s'", "'s", '#', '*']


def clean_word(word):
    for char in special_chars:
        if char in word:
            word = word.replace(char, '')

    return word


# def find_top_occurrences(word_map):
#     top_occurrences = []
#     for word, count in word_map.items():
#         if len(top_occurrences) < 5:
#             top_occurrences.append((word, count))
#             continue
#
#         top_occurrences = sorted(top_occurrences, key=lambda x: x[1], reverse=True)
#         if count > top_occurrences[-1][1]:
#             top_occurrences.pop()
#             top_occurrences.append((word, count))

# def find_top_occurrences(word_map):
#     return sorted(word_map.items(), key=lambda x: x[1], reverse=True)[:5]

def find_top_occurrences(word_map):
    return heapq.nlargest(5, word_map.items(), lambda x: x[1])


def line_words(line):
    word_map = defaultdict(int)
    if not line:
        return

    words = line.strip().split()
    for word in words:
        word = clean_word(word)
        if not word:
            continue

        word_map[word] += 1

    return list(word_map.items())


if __name__ == '__main__':
    with Pool(5) as p:
        with open('mytext.txt', 'r') as f:
            # because we use a generator the processes will not overlap :)
            results = p.map(line_words, (line for line in f))
            # print(results)

        word_map = defaultdict(int)
        for res in results:
            if not res:
                continue

            # print(res)

            for word, count in res:
                word_map[word] += count

        final_result = find_top_occurrences(word_map)
        print(final_result)
