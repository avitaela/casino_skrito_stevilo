vneseno_geslo = raw_input ("Vnesi geslo za skrivni nacrt:")

while True:
    if vneseno_geslo == "skrivnogeslo":
        print("Izspisek nacrta")
        break
    else:
        print("Geslo ni pravilno")
        vneseno_geslo = raw_input("Ponovno vnesi geslo")
print("Konec programa.")

