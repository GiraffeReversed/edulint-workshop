def greatest_common_divisor(a, b):
    a_dividor = 0
    b_dividor = 0
    common_dividor = 0
    Range_num = 0
    if a > b:
        Range_num = a
    else:
        Range_num = b
    for i in range(1, Range_num + 1):
        if a % i == 0:
            if i > a_dividor:
                a_dividor = i
                #print('a', a_dividor)
        if b % i == 0:
            if i > b_dividor:
                b_dividor = i
                #print('b', b_dividor)
        if a_dividor == b_dividor:
            common_dividor = a_dividor
            #print('c', common_dividor)
    return common_dividor
