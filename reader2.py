
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

        self.hc1 = None
        self.hc2 = None
        self.hc3 = None

        self.wc1 = None
        self.wc2 = None
        self.wc3 = None
        self.wc4 = None

        self.p1 = None
        self.p2 = None
        self.p3 = None
        self.p4 = None
        self.p5 = None
        self.p6 = None

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

def add_hoorcollege(vak):
    aantal = vakken[vak].hoorcolleges
    if (aantal >= 1):
        vakken[vak].hc1 = vakken[vak].vak + ": hoorcollege1"
    if (aantal >= 2):
        vakken[vak].hc2 = vakken[vak].vak + ": hoorcollege2"
    if (aantal == 3):
        vakken[vak].hc3 = vakken[vak].vak + ": hoorcollege3"

def add_werkcollege(vak):
    aantal = vakken[vak].aantal_werkcolleges
    if (aantal >= 1):
        vakken[vak].wc1 = vakken[vak].vak + ": werkcollege1"
    if (aantal >= 2):
        vakken[vak].wc2 = vakken[vak].vak + ": werkcollege2"
    if (aantal >= 3):
        vakken[vak].wc3 = vakken[vak].vak + ": werkcollege3"
    if (aantal == 3):
        vakken[vak].wc4 = vakken[vak].vak + ": werkcollege4"

def add_practica(vak):
    aantal = vakken[vak].aantal_practica
    if (aantal >= 1):
        vakken[vak].p1 = vakken[vak].vak + ": practica1"
    if (aantal >= 2):
        vakken[vak].p2 = vakken[vak].vak + ": practica2"
    if (aantal >= 3):
        vakken[vak].p3 = vakken[vak].vak + ": practica3"
    if (aantal >= 4):
        vakken[vak].p4 = vakken[vak].vak + ": practica4"
    if (aantal >= 5):
        vakken[vak].p5 = vakken[vak].vak + ": practica5"
    if (aantal == 6):
        vakken[vak].p6 = vakken[vak].vak + ": practica6"


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
    add_hoorcollege(vak)
    add_werkcollege(vak)
    add_practica(vak)
