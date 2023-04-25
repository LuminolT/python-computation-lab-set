import pandas as pd

from word_counter import WordCounter
from trie_tree import trie2dict
from typing import List


def generate_table(file_path: str, key_words: List[str]) -> pd.DataFrame:
    structures = ['dict', 'trie']
    results = {}

    for structure in structures:
        wc = WordCounter('./lab-1/sublab-4/benchmark_texts/' +
                         file_path, key_words, structure)
        results[structure] = wc.count()

    return pd.DataFrame({
        'file_name': [file_path],
        'dict_time': [results['dict'][1]],
        'trie_time': [results['trie'][1]],
        'dict_size': [results['dict'][2]],
        'trie_size': [results['trie'][2]],
        'consistency': ['Yes' if trie2dict(results['trie'][0]) == results['dict'][0] else 'No']
    })


def main():

    line_length = 80

    file_paths = ['5.txt', '10.txt', '15.txt', '20.txt',
                  '1k.txt', '10k.txt', '100k.txt', '1000k.txt']

    table = pd.DataFrame(
        columns=['file_name', 'dict_time', 'trie_time', 'dict_size', 'trie_size', 'consistency'])

    for file_path in file_paths:
        print('\r Processing file: {}'.format(file_path), end='')
        table = pd.concat([table, generate_table(file_path, None)])

    print('\r' + '-' * line_length)
    print('Benchmark Results with no key words: ')
    print(table)

    print('-' * line_length)

    table = pd.DataFrame(
        columns=['file_name', 'dict_time', 'trie_time', 'dict_size', 'trie_size', 'consistency'])

    for file_path in file_paths:
        print('\r Processing file: {}'.format(file_path), end='')
        table = pd.concat([table, generate_table(
            file_path, ['good', 'take', 'be', 'one', 'get'])])

    print('\r' + '-' * line_length)
    print('Benchmark Results with key words: ')
    print(table)

    print('-' * line_length)


if __name__ == "__main__":
    main()
