import numpy as np
import time


def reverse_1():
    start_time = time.time()

    # with open('./words.txt', 'r') as file:
    #     lines = file.readlines()

    # FEAT: Change the working path.
    with open('./lab-1/sublab-3/words.txt', 'r') as file:
        lines = file.readlines()

    # Remove '\n' and convert text from list to set
    text = [line.strip('\n') for line in lines]
    textset = set(text)

    revlist = []
    # Traverse word in text and print word which is in textset
    for word in text:
        if word[::-1] in textset:
            revlist.append(word)
    end_time = time.time()

    # Write reverse pairs into file
    with open('./lab-1/sublab-3/reverse_1.txt', 'w') as f:
        for word in revlist:
            f.write(word)
            f.write(' ')
            f.write(word[::-1])
            f.write('\n')

    return end_time - start_time, len(revlist)


def reverse_2():
    start_time = time.time()
    # with open('./words.txt', 'r') as file:
    #     lines = file.readlines()

    # FEAT: Change the working path.
    with open('./lab-1/sublab-3/words.txt', 'r') as file:
        lines = file.readlines()

    textlist = [line.strip('\n') for line in lines]
    # Create reverse textlist
    revlist = []
    for word in textlist:
        revlist.append(word[::-1])

    # Intersection of textset and revset
    textset = set(textlist)
    revset = set(revlist)
    rev_pair_set = textset & revset
    end_time = time.time()

    with open('./lab-1/sublab-3/reverse_2.txt', 'w') as f:
        for word in rev_pair_set:
            f.write(word)
            f.write(' ')
            f.write(word[::-1])
            f.write('\n')

    return end_time - start_time, len(rev_pair_set)


if __name__ == "__main__":
    time1, num1 = reverse_1()
    time2, num2 = reverse_2()
    print("Costing time with reverse_1: {}".format(time1))
    print("Costing time with reverse_2: {}".format(time2))
    print("Number of reversed pairs with reverse_1: {}".format(num1))
    print("Number of reversed pairs with reverse_2: {}".format(num2))
