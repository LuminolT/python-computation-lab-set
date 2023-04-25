'''
Author: LuminolT luminol.chen@gmail.com
Date: 2023-03-28 21:54:06
LastEditors: LuminolT luminol.chen@gmail.com
LastEditTime: 2023-03-28 23:20:06
FilePath: /python-computation-labs/lab-1/sublab-4/word_counter.py
Description: 

Copyright (c) 2023 by LuminolT, All Rights Reserved. 
'''
import os
import sys
import time
from trie_tree import *
from typing import Tuple, Dict, List


class WordCounter:

    def __init__(self, path: str, key_words: List[str], method: str = 'trie'):
        assert os.path.exists(path)
        assert method in ['trie', 'dict']
        self.path = path
        self.method = method
        self.key_words = key_words

    def count(self):
        if self.method == 'trie':
            return self._count_trie()
        else:
            return self._count_dict()

    def _count_trie(self) -> Tuple[TrieTree, float, int]:
        with open(self.path, 'r') as f:
            start_time = time.time()
            trie = TrieTree()
            for line in f:
                for word in line.split():
                    if self.key_words is not None and word not in self.key_words:
                        continue
                    trie.insert(word)
            end_time = time.time()
            return trie, end_time - start_time, sys.getsizeof(trie)

    def _count_dict(self) -> Tuple[Dict[str, int], float, int]:
        with open(self.path, 'r') as f:
            start_time = time.time()
            d = {}
            for line in f:
                for word in line.split():
                    if self.key_words is not None and word not in self.key_words:
                        continue
                    if word not in d:
                        d[word] = 0
                    d[word] += 1
            end_time = time.time()
            return d, end_time - start_time, sys.getsizeof(d)
