from classes import vak, werkgroep, hoorcollege, practica, lokaal, dag, tijdslot, student

def read_files(): 
	
	# studentenfile lezen
	f = open('studentenenvakken.csv', 'r')
	
	# lijst waar student objecten in gaan
	studenten = []

	# loop over alle regels heen
	for line in f:
	    line = line.split(',')
	    studentennummer = line[2]
	    
	    # lijst waar inschrijvingen in gaan
	    inschrijvingen = []
		
		# loop om de lijst te vullen	    
	    for i in range(3, 8):
	    	if line[i] != None:
	    		inschrijvingen.append(line[i])

	    # maak student object aan en stop het in studenten
	    stdent = student(studentennummer, inschrijvingen)
	    studenten.append(stdent)

###########################################################################

	# lokalenfile lezen
	e = open('lokalen.txt', 'r')
	
	# lijst met lokaal objecten
	lokalen = []

	# loop over alle regels heen
	for line in e:
		line = line.split('\t')
	    
		# naam & capaciteit voor object lokaal
		naam = line[0]
		capaciteit = line[1]

	    # dagen en tijden maken
		tijden = []
		dagen = []
		for i in range(4):
			tijdslot_temp = tijdslot(i, None) 
			tijden.append(tijdslot_temp)
		for i in range(5):
			dag_temp = dag(i, tijden)
			dagen.append(dag_temp)

	    # lokaal toevoegen aan lokalen lijst
		lkaal = lokaal(naam, capaciteit, dagen)
		lokalen.append(lkaal)

###########################################################################

	# vakkenfile lezen
	d = open('vakken.txt', 'r')
	
	# lijsten waar de objecten in gaan
	vakken = []

	# loop over alle regels heen
	for line in d:
		line = line.split('\t')
	    
		hoorcolleges = []
		werkgroepen = []
		practicas = []

	    # naam voor vak object
		naam = line[0]
	    
		# variabele voor totaal aantal studenten in het vak
		aantal = aantal_studenten(naam, studenten, inschrijvingen)

		# hoorcollege objecten maken
		aantal_hoorcolleges = line[1]
		if aantal_hoorcolleges != None:
			for i in range(int(aantal_hoorcolleges)):
				hc_naam = naam + '  HC-' + str(i)
				hoorcollege_temp = hoorcollege(hc_naam, aantal)
				hoorcolleges.append(hoorcollege_temp)
	    		
	    # werkcollege objecten maken
		if line[2] != '0' and aantal != 0: 
			aantal_werkcolleges = int(line[2])
			max_werkcolleges = int(line[3].rstrip('\n'))
			instanties = aantal / (max_werkcolleges)
			if (aantal % max_werkcolleges > 0):
				instanties += 1	
			studenten_per_instantie = aantal / instanties
			for i in range(instanties):
				wg_naam  = naam + '  WG-' + str(i)
				werkgroep_temp = werkgroep(naam, studenten_per_instantie)
				werkgroepen.append(werkgroep_temp)

		else:
			werkcolleges = None

		# practica objecten maken
		if line[4] != '0' and aantal != 0:
			aantal_practica = int(line[4])
			max_practica = int(line[5].rstrip('\n'))
			instanties = aantal / max_practica
			if (aantal % max_practica > 0):
				instanties += 1
			studenten_per_instantie = aantal / instanties
			for i in range(instanties):
				pr_naam = naam + '  PR-' + str(i)
				practica_temp = practica(i, studenten_per_instantie)
				practicas.append(practica_temp)

		else:
			practicas = None

	    # vak object maken
		vk = vak(naam, aantal, hoorcolleges, werkgroepen, practicas)
		vakken.append(vk)

	# totaal aantal in te delen vakken
	totaal_lessen = 0
	totaal_hoorcolleges = 0
	totaal_werkgroepen = 0
	totaal_practica = 0

	for i in range(len(vakken)):
		if vakken[i].hoorcolleges != None:
			for j in range(len(vakken[i].hoorcolleges)):
				totaal_hoorcolleges += 1
				totaal_lessen += 1
		if vakken[i].werkgroepen != None:
			for k in range(len(vakken[i].werkgroepen)):
				totaal_werkgroepen += 1
				totaal_lessen += 1
		if vakken[i].practicas != None:
			for l in range(len(vakken[i].practicas)):
				totaal_practica += 1
				totaal_lessen += 1	

	# eerst hoorcolleges die > 60 roosteren
	grootste_roosteren(vakken, hoorcolleges, lokalen)

	for j in range(len(lokalen[5].dagen)):
		for k in range(len(lokalen[5].dagen[j].tijden)):
			print lokalen[5].dagen[j].tijden[k].les
####################################################################################################

# functie om het aantal studenten in een vak uit te rekenen
def aantal_studenten(vak, studenten, inschrijvingen):
	vak_aantal = 0
	
	for student in studenten:
		for i in range(len(student.inschrijvingen)):
			if student.inschrijvingen[i] == vak:
				vak_aantal += 1

	return vak_aantal

###################################################################################################

# functie om lessen in te roosteren
def grootste_roosteren(vakken, hoorcolleges, lokalen):
	
	# lijst om hoorcolleges in op te slaan
	grootste_hoorcolleges = []
	for i in range(len(vakken)):
		for j in range(len(vakken[i].hoorcolleges)):
			if vakken[i].hoorcolleges[j].studenten > 60:
				grootste_hoorcolleges.append(vakken[i].hoorcolleges[j])
	
	
	
	# rooster de grootste in
	for i in range(len(grootste_hoorcolleges)):
			for l in range(len(vakken)):
				for m in range(len(vakken[l].hoorcolleges)):
					if vakken[l].hoorcolleges[m].naam == grootste_hoorcolleges[i].naam:
						vakken[l].hoorcolleges[m] = grootste_hoorcolleges[i]
			for j in range(len(lokalen[5].dagen)):
				for k in range(len(lokalen[5].dagen[j].tijden)):
					if lokalen[5].dagen[j].tijden[k].les == None \
						and grootste_hoorcolleges[i].les == False:
						lokalen[5].dagen[j].tijden[k].les = grootste_hoorcolleges[i].naam
						grootste_hoorcolleges[i].les = True
						print lokalen[5].dagen[j].tijden[k]