def count_a(text):
    a=0
    for i in range(len(text)):
        if text[i]=="a" or text[i]=="A":
            a=a+1
    return a
