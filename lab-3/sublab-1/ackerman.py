'''
Author: LuminolT luminol.chen@gmail.com
Date: 2023-05-06 06:17:07
LastEditors: LuminolT luminol.chen@gmail.com
LastEditTime: 2023-05-06 10:28:05
FilePath: /lab-3/sublab-1/ackerman.py
Description: 

Copyright (c) 2023 by LuminolT, All Rights Reserved. 
'''


def ackermann(m: int, n: int) -> int:
    """
        Ackerman function.
    """
    if m < 0 or n < 0:
        raise ValueError("Not Positive Interger")
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m-1, 1)
    else:
        return ackermann(m-1, ackermann(m, n-1))


print(ackermann(4, 1))
