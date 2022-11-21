def main(password):
    valid = True
    num = False
    symb = False
    upper_l = False
    lower_l = False
    for i in range(0, len(password)):
        asc_i = ord(password[i])
        if (asc_i >= 32 and asc_i <= 47) or (asc_i >= 58 and asc_i <= 64) or (asc_i >= 91 and asc_i <= 96):
            symb = True
            #print("Symbol")
        elif (asc_i >= 48 and asc_i <= 57):
            num = True
            #print("Number")
        elif (asc_i >= 65 and asc_i <= 90):
            upper_l = True
            #print("Uppercase letter")
        elif (asc_i >= 97 and asc_i <= 122):
            lower_l = True
            #print("Lowercase letter")
    if symb == False or num == False or upper_l == False or lower_l == False:
        valid = False
    return valid