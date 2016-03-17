skrita_stevilka = raw_input ("Ugani skrito stevilo:")

while True:
    if skrita_stevilka == 25:
        print "Cestitam, uganil si skrito stevilko"
        break
    elif skrita_stevilka < 25:
        print "Skrita stevilka je vecja."
        skrita_stevilka = raw_input ("Ponovno vnesi stevilko:")
else:
        print "Skrita stevilka je manjsa."
        skrita_stevilka = raw_input ("Ponovno vnesi stevilko.")
print "Konec programa."