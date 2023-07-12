def convertir (ch):
    ch2=''
    for i in ch:
        if (i == ","):
            ch2=ch2+"."
        else :
            ch2=ch2+i
    ch2=float(ch2)
    print (ch2)
    return (ch2)
convertir ("5,54556")