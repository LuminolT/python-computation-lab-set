'''
Author: LuminolT luminol.chen@gmail.com
Date: 2023-05-06 06:42:54
LastEditors: LuminolT luminol.chen@gmail.com
LastEditTime: 2023-05-06 06:46:50
FilePath: /lab-3/sublab-1/duplicate.py
Description: 

Copyright (c) 2023 by LuminolT, All Rights Reserved. 
'''


import random


def remove_duplicates(seq: list) -> list:
    """
    Remove the duplicated items from a sequence object.
    """
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


# generate random list and dict
lst = [random.randint(1, 10) for _ in range(10)]
dct = {f'key_{random.randint(1, 10)}': random.randint(1, 100)
       for _ in range(10)}

# remove duplicates
lst_unique = remove_duplicates(lst)
dct_unique = {k: v for k, v in zip(remove_duplicates(
    dct.keys()), remove_duplicates(dct.values()))}

# result
print('list object')
print(f'before: {lst}')
print(f'after : {lst_unique}')

print('dict object')
print(f'before: {dct}')
print(f'after : {dct_unique}')
