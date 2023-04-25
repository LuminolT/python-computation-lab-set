'''res_trie
Author: LuminolT luminol.chen@gmail.com
Date: 2023-03-28 12:50:18
LastEditors: LuminolT luminol.chen@gmail.com
LastEditTime: 2023-03-28 22:46:22
FilePath: /python-computation-labs/lab-1/sublab-4/text_generator.py
Description: 

Copyright (c) 2023 by LuminolT, All Rights Reserved. 
'''
import argparse
import random

words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can',
         'like', 'time', 'no', 'just', 'him', 'know', 'take', 'person', 'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us']


def generate_random_word() -> str:
    return words[random.randint(0, len(words)-1)]


def generate_random_text(length: int) -> str:
    text = ""

    for i in range(length):
        text += generate_random_word() + ' '

    return text


def main():
    parser = argparse.ArgumentParser(description='Generate random text.')
    parser.add_argument('-l', '--length', type=int, default=5,
                        help='length of the article')
    parser.add_argument('-s', '--save', type=str, default=None,
                        help='path to save the generated text')
    args = parser.parse_args()

    generated_text = generate_random_text(args.length)

    if args.save:
        with open(args.save, 'w') as f:
            f.write(generated_text)
    else:
        print(generated_text)


if __name__ == "__main__":
    main()
