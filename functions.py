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
			tijdslot_temp = tijdslot(i, False) 
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

		# totaal aantal lessen in het vak
		lessen = 0

		# hoorcollege objecten maken
		aantal_hoorcolleges = line[1]
		if aantal_hoorcolleges != None:
			for i in range(int(aantal_hoorcolleges)):
				hc_naam = naam + '  HC-' + str(i)
				hoorcllege = hoorcollege(hc_naam, aantal)
				hoorcolleges.append(hoorcllege)
				lessen += 1
	    		
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
				wrkgroep = werkgroep(wg_naam, studenten_per_instantie)
				werkgroepen.append(wrkgroep)
				lessen += 1

		else:
			#werkcolleges = False
			werkgroepen = []

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
				prctica = practica(pr_naam, studenten_per_instantie)
				practicas.append(prctica)
				lessen += 1

		else:
			#practicas = False
			practicas = []

		# dagen en tijden maken
		tijden = []
		dagen = []
		for i in range(4):
			tijdslot_temp = tijdslot(i, False) 
			tijden.append(tijdslot_temp)
		for i in range(5):
			dag_temp = dag(i, tijden)
			dagen.append(dag_temp)

	    # vak object maken
		vk = vak(naam, aantal, hoorcolleges, werkgroepen, practicas, lessen, dagen)
		vakken.append(vk)

	# totaal aantal in te delen vakken
	totaal_lessen = 0
	totaal_hoorcolleges = 0
	totaal_werkgroepen = 0
	totaal_practica = 0

	for i in range(len(vakken)):
		if vakken[i].hoorcolleges:
		#if vakken[i].hoorcolleges != False:
			for j in range(len(vakken[i].hoorcolleges)):
				totaal_hoorcolleges += 1
				totaal_lessen += 1
		if vakken[i].werkgroepen:
		#if vakken[i].werkgroepen != False:
			for k in range(len(vakken[i].werkgroepen)):
				totaal_werkgroepen += 1
				totaal_lessen += 1
		if vakken[i].practicas:
		#if vakken[i].practicas != False:
			for l in range(len(vakken[i].practicas)):
				totaal_practica += 1
				totaal_lessen += 1	

	# grootste lokalen eerst inroosteren  
	# passen in totaal 20 lessen in een week
	#for z in range(0, 19):
		
		# eerst de grootste zoeken
		#for i in range(len(vakken)):
			#volste_hoorcollege = vakken[0].hoorcolleges[0].aantal_studenten
			#
				#for j in range(len(vakken[i].hoorcolleges)):
					# volste vervangen indien groter
					#if vakken[i].hoorcolleges[j].studenten > volste_hoorcollege
					#and vakken[i].hoorcolleges[j].les == False:
					#	volste_hoorcollege = vakken[i].hoorcolleges[j].studenten
					#	vak_temp = i
					#	hc_temp = j
		
		# rooster grootste hoorcollege in
		
	## PRESENTATIE INFORMATIE
	totaal_studenten = range(len(studenten))
	totaal_vakken = range(len(vakken))
	totaal_lokalen = range(len(lokalen))
		
	count_temp = 0	
	count_2 = 0			
	for i in range(len(vakken)):
		if vakken[i].hoorcolleges:
		#if vakken[i].hoorcolleges != False:

			for j in range(len(vakken[i].hoorcolleges)):
				
				count_temp += 1
		if vakken[i].werkgroepen:
		#if vakken[i].werkgroepen != False:
			for j in range(len(vakken[i].werkgroepen)):
				
				count_temp += 1
		if vakken[i].practicas:
		#if vakken[i].practicas != False:		
			for j in range(len(vakken[i].practicas)):
				count_temp += 1
	

	# de rest van de vakken inroosteren
	for i in range(len(lokalen)):
		for j in range(len(lokalen[i].dagen)):
			for k in range(len(lokalen[i].dagen[j].tijden)):
				print lokalen[i].dagen[j].tijden[k].les
				if lokalen[i].dagen[j].tijden[k].les == False:
					random = vak_kiezen(vakken)
					print random
					lokalen[i].dagen[j].tijden[k].les = random

# functie om het aantal studenten in een vak uit te rekenen
def aantal_studenten(vak, studenten, inschrijvingen):
	vak_aantal = 0
	
	for student in studenten:
		for i in range(len(student.inschrijvingen)):
			if student.inschrijvingen[i] == vak:
				vak_aantal += 1

	return vak_aantal

# functie om een vak te kiezen
def vak_kiezen(vakken):

	nieuw_vak = 0

	for i in range(len(vakken)):
		if vakken[i].hoorcolleges:
		#if vakken[i].hoorcolleges != False:
			for j in range(len(vakken[i].hoorcolleges)):
				if vakken[i].hoorcolleges[j].les == False:
					nieuw_vak = vakken[i].hoorcolleges[j].naam
					vakken[i].hoorcolleges[j].les = True
					return nieuw_vak

		if vakken[i].werkgroepen:
		#if vakken[i].werkgroepen != False:
			for k in range(len(vakken[i].werkgroepen)):
				if vakken[i].werkgroepen[k].les == False:
					nieuw_vak = vakken[i].werkgroepen[k].naam
					vakken[i].werkgroepen[k].les = True
					return nieuw_vak

		if vakken[i].practicas:
		#if vakken[i].practicas != False:
			for l in range(len(vakken[i].practicas)):
				if vakken[i].practicas[l].les == False:
					nieuw_vak = vakken[i].practicas[l].naam
					vakken[i].practicas[l].les = True
					return nieuw_vak
