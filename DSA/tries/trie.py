import json


class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = '*'

    def add(self, word):
        current = self.root
        for c in word:
            if c not in current:
                current[c] = {}

            current = current[c]

        current[self.end_symbol] = True

    def exist(self, word):
        current = self.root
        for c in word:
            if c not in current:
                return False

            current = current[c]

        return current.get(self.end_symbol, False)

    def search_level(self, current, prefix, words):
        if self.end_symbol in current:
            words.append(prefix)

        for c in sorted(key for key in current.keys() if key != self.end_symbol):
            self.search_level(current[c], prefix + c, words)

    def words_with_prefix(self, prefix):
        words = []
        current = self.root
        for c in prefix:
            if c not in current:
                return []

            current = current[c]

        self.search_level(current, prefix, words)
        return words

    def find_matches(self, document):
        matches = set()
        for i in range(len(document)):
            current = self.root
            for j in range(i, len(document)):
                c = document[j]
                if c not in current:
                    break

                current = current[c]
                if self.end_symbol in current:
                    matches.add(document[i:j + 1])

        return matches




def main():
    trie = Trie()
    for word in ['hello', 'hell', 'hi', 'dev', 'devops', 'development']:
        trie.add(word)

    print(json.dumps(trie.root, indent=4))
    print(trie.exist('hell'))
    print(trie.exist('hellcat'))
    print(trie.exist('de'))
    print(trie.exist('dev'))

    print(trie.words_with_prefix('de'))

    document = 'hello my fellow developer'
    print(trie.find_matches(document))


if __name__ == '__main__':
    main()
