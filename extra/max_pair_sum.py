def max_pair_sum(num_list):
    r = 0
    for i in range(0, len(num_list)):
        try:
            if num_list[i] + num_list[i+1] > r:
                r = num_list[i] + num_list[i+1]

            else:
                pass
        except:
            pass
    return r
