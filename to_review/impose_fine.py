def impose_fine(age, beer):
    if age < 18 and beer == True:
        impose_fine = True
    else:
        impose_fine = False
    return impose_fine
