import time

def Input_word_list(filename):
    with open(filename) as file:
        data = file.read().split('\n')
        word_dict = dict.fromkeys(data,0)
    return word_dict

def cuttable(word_dict, word):
    for i in range(len(word)):
        word_l = list(word)
        word_l.pop(i)
        word_cut = ''.join(word_l)
        if word_cut in word_dict.keys():
            if word_dict[word_cut] == 1:
                word_dict[word] = 1
                return 1
            else:
                word_dict[word] = cuttable(word_dict, word_cut)
        if word_cut == 'a' or word_cut == 'i':
            word_dict[word] = 1
            return 1
        

def main():
    filename = "./lab-2/sublab-4/words.txt"
    my_word_dict = Input_word_list(filename)
    # print(word_dict)
    longest=''
    start_time = time.time()
    for key in my_word_dict.keys():
        cuttable(my_word_dict, key)
        if my_word_dict[key] == 1 and len(key) >= len(longest):
            longest = key

    print(longest)
    end_time = time.time()
    print(end_time-start_time)
    PrintLongest(my_word_dict, longest)

def PrintLongest(word_dict, word):
    for i in range(len(word)):
        word_l = list(word)
        word_l.pop(i)
        word_cut = ''.join(word_l)
        if word_cut in word_dict.keys():
            if word_dict[word_cut] == 1:
                print('-->', word_cut)
            PrintLongest(word_dict, word_cut)
        if word_cut == 'a':
            print('-->', 'a')
            return 1   
        if word_cut == 'i':
            print('-->', 'i')
            return 1 
    

if __name__ == "__main__":
    main()


    