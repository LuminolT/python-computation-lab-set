from random import randint

# def classgen(N):
#     newclass = []
#     for i in range(N):
#         newclass.append(randint(1, 366))

#     return tuple(sorted(newclass))


# if __name__ == "__main__":
#     M = int(input("M="))
#     N = int(input("N="))
#     classdict = {}
#     Q = 0
#     for i in range(M):
#         newclass = classgen(N)
#         if newclass in classdict:
#             classdict[newclass] += 1
#         else:
#             classdict[newclass] = 1
#     for key, value in classdict.items():
#         if value > 1:
#             Q += value

if __name__ == '__main__':
    M= int(input("M="))
    N= int(input("N="))
    Q=0
    for i in range(M):
        classdict = set()
        for j in range(N):
            birth=randint(1,366)
            if birth in classdict:
                Q+=1
                break
            else:
                classdict.add(birth)

    P = Q / M
    print(P)
    print(format(P * 100, ".2f"), "%")
