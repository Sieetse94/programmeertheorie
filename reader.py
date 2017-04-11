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

        self.tijd1 = False
        self.tijd2 = False
        self.tijd3 = False
        self.tijd4 = False
        self.tijd5 = False
        self.tijd6 = False
        self.tijd7 = False
        self.tijd8 = False
        self.tijd9 = False
        self.tijd10 = False
        self.tijd11 = False
        self.tijd12 = False
        self.tijd13 = False
        self.tijd14 = False
        self.tijd15 = False
        self.tijd16 = False
        self.tijd17 = False
        self.tijd18 = False
        self.tijd19 = False
        self.tijd20 = False

class vakgegevens:

    def __init__(self, vak, hoorcolleges, werkcolleges, max_werkcolleges, practica, max_practica):
        self.vak = vak
        self.hoorcolleges = hoorcolleges
        self.werkcolleges = werkcolleges
        self.max_werkcolleges = max_werkcolleges
        self.practica = practica
        self.max_practica = max_practica


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
    vakkeh = vakgegevens(vak, hoorcolleges, werkcolleges, max_werkcolleges, practica, max_practica)
    vakken.append(vakkeh)

print(vakken[0].vak)

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
