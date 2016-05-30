def listoverlap(list1, list2):
    c = []
    for i in list1:
        for j in list2:
            if i == j:
                if j not in c:
                    c.append(j)
    return c


def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = listoverlap(a, b) # other c than in listoverlap
    print(c)
    return


if __name__ == '__main__':
    main()
