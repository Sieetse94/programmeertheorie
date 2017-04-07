class studentengegevens:

    def __init__(self, achternaam, naam, studentennummer, vak1, vak2, vak3, vak4, vak5):
        self.achternaam = achternaam
        self.naam = naam
        self.studentennummer = studentennummer
        self.vak1 = vak1
        self.vak2 = vak2
        self.vak3 = vak3
        self.vak4 = vak6
        self.vak5 = vak5

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

student = []

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
    student.append(students)

print(student[5].achternaam)

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

print(vakken[3].max_werkcolleges)
