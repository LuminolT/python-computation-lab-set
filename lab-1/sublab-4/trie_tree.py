'''
Author: LuminolT luminol.chen@gmail.com
Date: 2023-03-28 21:44:42
LastEditors: LuminolT luminol.chen@gmail.com
LastEditTime: 2023-03-28 23:11:06
FilePath: /python-computation-labs/lab-1/sublab-4/trie_tree.py
Description: 

Copyright (c) 2023 by LuminolT, All Rights Reserved. 
'''


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0


class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def __getitem__(self, word: str) -> int:
        return self._search(word)

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.count += 1

    def _search(self, word: str) -> int:
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count


def trie2dict(trie: TrieTree) -> dict:
    def dfs(node: TrieNode, path: str, d: dict):
        if node.count > 0:
            d[path] = node.count
        for char, child in node.children.items():
            dfs(child, path + char, d)
    d = {}
    dfs(trie.root, '', d)
    return d
