def dobro(moeda, formato=False):
    dob = moeda * 2
    #return format(dob)
    if not formato:
        return dob
    else:
        return format(dob)
