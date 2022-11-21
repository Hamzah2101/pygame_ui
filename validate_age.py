def main(age):
    valid = True
    try:
        int(age)
    except ValueError:
        valid = False
    if valid == True:
        if int(age) <= 0:
            valid = False
    return valid
