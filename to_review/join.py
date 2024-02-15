def join(text1, text2):
    if len(text1) <= len(text2):
        sum_text = text1+text2
    else:
        sum_text = text2 + text1
    result =""
    for i in range (len(sum_text)):
        result += sum_text[i]
    return result
