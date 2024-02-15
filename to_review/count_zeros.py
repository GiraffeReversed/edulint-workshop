def count_zeros(table):
    x = 0
    for i in range(len(table)):
        if 0 in table[i]:
            for j in range(len(table[i])):
                if ((table[i])[j]) == 0:
                    x += 1
                else:
                    continue
        else:
            continue
        return(x)
