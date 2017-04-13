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

    def __init__(self, vak, hoorcolleges, werkcolleges, max_werkcolleges, practica, max_practica, studentenaantal):
        self.vak = vak
        self.hoorcolleges = hoorcolleges
        self.werkcolleges = werkcolleges
        self.max_werkcolleges = max_werkcolleges
        self.practica = practica
        self.max_practica = max_practica
        self.studentenaantal = studentenaantal


        # werkcolleges, hcs en practica indelen
        #self.werkcollege1 =
        #self.hoorcollege =
        #self.werkcollege2 =


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

print(studenten[0].achternaam)

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

print(vakken[5].studentenaantal, vakken[5].vak)

# lokalen scrapen

e = open('lokalen.txt', 'r')

lokalen = []

for line in e:
    line = line.split('\t')
    naam = line[0]
    max_capaciteit = line[1]
    lokaleh = lokaalgegevens(naam, max_capaciteit)
    lokalen.append(lokaleh)

print(lokalen[5].tijd16)
