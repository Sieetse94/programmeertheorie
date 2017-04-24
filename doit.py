class vakgegevens:

    def __init__(self, vak, hoorcolleges, werkcolleges, max_werkcolleges, practica, max_practica, studentenaantal, werkcollege):
        self.vak = vak
        self.hoorcolleges = hoorcolleges
        self.werkcolleges = werkcolleges
        self.max_werkcolleges = max_werkcolleges
        self.practica = practica
        self.max_practica = max_practica
        self.studentenaantal = studentenaantal
        self.werkcollege = werkcollege
        i = 1
        print(max_werkcolleges)
        self.werkcollege.append(studentenaantal)

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
    werkcollege = []
    vakkeh = vakgegevens(vak, hoorcolleges, werkcolleges, max_werkcolleges, practica, max_practica, studentenaantal, werkcollege)
    vakken.append(vakkeh)

print(vakken[5].studentenaantal, vakken[5].vak)
