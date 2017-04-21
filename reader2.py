
class studentengegevens:

    def __init__(self, achternaam, naam, studentennummer, vak1, vak2, vak3, vak4, vak5):
        self.achternaam = achternaam
        self.naam = naam
        self.studentennummer = studentennummer
        self.vak1 = vak1
        self.vak2 = vak2
        self.vak3 = vak3
        self.vak4 = vak4
        self.vak5 = vak5

class lokaalgegevens:
    def __init__(self, naam, max_capaciteit):
        self.naam = naam
        self.max_capaciteit = max_capaciteit

        self.tijd1 = None
        self.tijd2 = None
        self.tijd3 = None
        self.tijd4 = None
        self.tijd5 = None
        self.tijd6 = None
        self.tijd7 = None
        self.tijd8 = None
        self.tijd9 = None
        self.tijd10 = None
        self.tijd11 = None
        self.tijd12 = None
        self.tijd13 = None
        self.tijd14 = None
        self.tijd15 = None
        self.tijd16 = None
        self.tijd17 = None
        self.tijd18 = None
        self.tijd19 = None
        self.tijd20 = None

class vakgegevens:
    vakkenlijst = []

    def __init__(self, vak, hoorcolleges, werkcolleges, max_werkcolleges, practica, max_practica, studentenaantal):
        self.vak = vak
        self.vakkenlijst.append(self)
        self.hoorcolleges = hoorcolleges
        self.werkcolleges = werkcolleges
        self.max_werkcolleges = max_werkcolleges
        self.aantal_werkcolleges = aantal_werkcolleges
        self.practica = practica
        self.max_practica = max_practica
        self.aantal_practica = aantal_practica
        self.studentenaantal = studentenaantal
        self.werkcollege_lijst = []
        self.practica_lijst = []

def aantal_studenten(vak):
    vak_aantal = 0
    for i in range(len(studenten)):
        if (studenten[i].vak1 == vak):
            vak_aantal += 1
        if (studenten[i].vak2 == vak):
            vak_aantal += 1
        if (studenten[i].vak3 == vak):
            vak_aantal += 1
        if (studenten[i].vak4 == vak):
            vak_aantal += 1
        if (studenten[i].vak5 == vak):
            vak_aantal += 1
    return vak_aantal


# werkcolleges uitrekenen
def aantal_werkcolleges(vak):
    if (vakken[vak].max_werkcolleges.rstrip('\n') == 'nvt'):
        return
    else:
        werkcolleges = 0
        aantal = vakken[vak].studentenaantal
        maxi = int(vakken[vak].max_werkcolleges.rstrip('\n'))
        werkcolleges = aantal / maxi
        if (aantal % maxi > 0):
            werkcolleges += 1
        return werkcolleges
   

# practica uitrekenen
def aantal_practica(vak):  
    if vakken[vak].max_practica.rstrip('\n') == 'nvt':
        return
    else:
        practica = 0
        aantal = vakken[vak].studentenaantal
        maxi = int(vakken[vak].max_practica.rstrip('\n'))
        practica = aantal / maxi
        if (aantal % maxi > 0):
            practica += 1
        return practica 

def add_werkcollege(vak):
    if vakken[vak].aantal_werkcolleges == None:
        return
    else: 
        lijst = []
        for j in range(int(vakken[vak].aantal_werkcolleges)):
            wc = "1." + str(j + 1)
            lijst.append(wc)
        return lijst   
                    
def add_practica(vak):
    if vakken[vak].aantal_practica == None:
        return
    else: 
        lijst = []
        for j in range(int(vakken[vak].aantal_practica)):
            wc = "1." + str(j + 1)
            lijst.append(wc)
        return lijst   

# studenten scrapen
f = open('studentenenvakken.csv', 'r')
studenten = []

for line in f:
    line = line.split(',')
    achternaam = line[0]
    naam = line[1]
    studentennummer = line[2]
    vak1 = line[3]
    vak2 = line[4]
    vak3 = line[5]
    vak4 = line[6]
    vak5 = line[7]
    students = studentengegevens(achternaam, naam, studentennummer, vak1, vak2, vak3, vak4, vak5)
    studenten.append(students)


# vakken scrapen
d = open('vakken.txt', 'r')
vakken = []

for line in d:
    line = line.split('\t')
    vak = line[0]
    hoorcolleges = line[1]
    werkcolleges = line[2]
    max_werkcolleges = line[3]
    practica = line[4]
    max_practica = line[5]
    studentenaantal = aantal_studenten(vak)
    vakkeh = vakgegevens(vak, hoorcolleges, werkcolleges, max_werkcolleges, practica, max_practica, studentenaantal)
    vakken.append(vakkeh)


# lokalen scrapen
e = open('lokalen.txt', 'r')
lokalen = []

for line in e:
    line = line.split('\t')
    naam = line[0]
    max_capaciteit = line[1]
    lokaleh = lokaalgegevens(naam, max_capaciteit)
    lokalen.append(lokaleh)


# aantal werkcolleges uitrekenen
for vak in range(len(vakken)):
    vakken[vak].aantal_werkcolleges = aantal_werkcolleges(vak)
    vakken[vak].aantal_practica = aantal_practica(vak)
    vakken[vak].werkcollege_lijst.append(add_werkcollege(vak))
    vakken[vak].practica_lijst.append(add_practica(vak))


 

# For zaal met de grootste capaciteit
# We moeten ervoor zorgen dat wij de zalen van groot naar klein in de classes indelen

for i in range(len(zalen)):

    # Hier moeten wij ervoor zorgen dat we 1 voor 1 de zalen van zalen[i] afgaan
    # Dit doen wij door de HCs, WCs en practica in te delen

    for j in range(len(vakken)):
        if (zalen[i].tijd1 != None):
            zalen[i].tijd1 = vakken[j].vaknaam
            vakken[j].hoorcollege1 = zalen[i].zaalnaam
            j += 1
        if (zalen[i].tijd2 != None):
            zalen[i].tijd2 = vakken[j].vaknaam
            vakken[j].hoorcollege1 = zalen[i].zaalnaam
            j += 1
        if (zalen[i].tijd3 != None):
            zalen[i].tijd3 = vakken[j].vaknaam
            vakken[j].hoorcollege1 = zalen[i].zaalnaam
            j += 1
        if (zalen[i].tijd4 != None):
            zalen[i].tijd4 = vakken[j].vaknaam
            vakken[j].hoorcollege1 = zalen[i].zaalnaam
            j += 1
        if (zalen[i].tijd5 != None):
            zalen[i].tijd5 = vakken[j].vaknaam
            vakken[j].hoorcollege1 = zalen[i].zaalnaam
            j += 1
        if (zalen[i].tijd6 != None):
            zalen[i].tijd6 = vakken[j].vaknaam
            vakken[j].hoorcollege1 = zalen[i].zaalnaam
            j += 1
        if (zalen[i].tijd7 != None):
            zalen[i].tijd7 = vakken[j].vaknaam
            vakken[j].hoorcollege1 = zalen[i].zaalnaam
            j += 1
        if (zalen[i].tijd8 != None):
            zalen[i].tijd8 = vakken[j].vaknaam
            vakken[j].hoorcollege1 = zalen[i].zaalnaam
            j += 1
        if (zalen[i].tijd9 != None):
            zalen[i].tijd9 = vakken[j].vaknaam
            vakken[j].hoorcollege1 = zalen[i].zaalnaam
            j += 1
        if (zalen[i].tijd10 != None):
            zalen[i].tijd10 = vakken[j].vaknaam
            vakken[j].hoorcollege1 = zalen[i].zaalnaam
            j += 1
        if (zalen[i].tijd11 != None):
            zalen[i].tijd11 = vakken[j].vaknaam
            vakken[j].hoorcollege1 = zalen[i].zaalnaam
            j += 1
        if (zalen[i].tijd12 != None):
            zalen[i].tijd12 = vakken[j].vaknaam
            vakken[j].hoorcollege1 = zalen[i].zaalnaam
            j += 1
        if (zalen[i].tijd13 != None):
            zalen[i].tijd13 = vakken[j].vaknaam
            vakken[j].hoorcollege1 = zalen[i].zaalnaam
            j += 1
        if (zalen[i].tijd14 != None):
            zalen[i].tijd14 = vakken[j].vaknaam
            vakken[j].hoorcollege1 = zalen[i].zaalnaam
            j += 1
        if (zalen[i].tijd15 != None):
            zalen[i].tijd15 = vakken[j].vaknaam
            vakken[j].hoorcollege1 = zalen[i].zaalnaam
            j += 1
        if (zalen[i].tijd16 != None):
            zalen[i].tijd16 = vakken[j].vaknaam
            vakken[j].hoorcollege1 = zalen[i].zaalnaam
            j += 1
        if (zalen[i].tijd17 != None):
            zalen[i].tijd17 = vakken[j].vaknaam
            vakken[j].hoorcollege1 = zalen[i].zaalnaam
            j += 1
        if (zalen[i].tijd18 != None):
            zalen[i].tijd18 = vakken[j].vaknaam
            vakken[j].hoorcollege1 = zalen[i].zaalnaam
            j += 1
        if (zalen[i].tijd19 != None):
            zalen[i].tijd19 = vakken[j].vaknaam
            vakken[j].hoorcollege1 = zalen[i].zaalnaam
            j += 1


    # Hier moet een functie komen die dit vervangt, uiteindelijk is het de bedoeling
    # dat de loop eerst alle tijden afgaat van een zaal totdat alle tijdslotten
    # bezet zijn.
    # Dan deel je eerst alle hoorcolleges1 in, daarna de hoorcolleges2, daarna werkcolleges enz.
    # Het moet uiteindelijk zo'n vorm hebben deelIn(input) *weet nog niet precies hoe maar komt goed
    #
# Om het uiteindelijk uit te printen, kunnen we voor nu zoiets gebruiken:

for i in range(len(vakken)):
    print(vakken[i].naam)
    print(printSchedule(vakken[i])


def printSchedule(vak):
    timeSchedule = []
    timeSchedule.append(self.tijd1, self.tijd2, ENZOVOORT)
    return timeSchedule

