
def size(cms, sex):
    if (cms < 36 and sex == 'female') or \
            (cms < 38 and sex == 'male'):
        return 'S'
    elif cms < 42:
        return 'M'
    else:
        return 'L'
