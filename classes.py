class vak(object):

	def __init__(self, naam, studenten, hoorcolleges, werkgroepen, practicas, lessen, dagen):
		self.naam = naam # uniek id
		self.studenten = studenten # aantal studenten in het vak
		self.hoorcolleges = hoorcolleges # lijst met hoorcollege objecten
		self.werkgroepen = werkgroepen # lijst met werkgroep objecten
		self.practicas = practicas # lijst met practica objecten
		self.lessen = lessen # totaal aantal lessen van dit vak
		self.dagen = dagen # lijst met dag objecten

class hoorcollege(object):

	def __init__(self, naam, studenten):
		self.naam = naam # uniek id
		self.studenten = studenten # aantal studenten in het hoorcollege
		self.les = False # ingedeeld of niet

class werkgroep(object):

	def __init__(self, naam, studenten):
		self.naam = naam # uniek id
		self.studenten = studenten # aantal studenten in de werkgroep
		self.les = False # ingedeeld of niet
		
class practica(object):

	def __init__(self, naam, studenten):
		self.naam = naam # uniek id
		self.studenten = studenten # aantal studenten in het practica
		self.les = False # ingedeeld of niet
		
########################################################

class lokaal(object):

	def __init__(self, naam, capaciteit, dagen):  
		self.naam = naam # uniek id
		self.capaciteit = capaciteit # totale capactieit van het lokaal
		self.dagen = dagen # dagen is een lijst met dag objecten


class dag(object):

	def __init__(self, naam, tijden): 
		self.naam = naam # uniek id
		self.tijden = tijden # tijden is een lijst met tijdslot objecten
		


class tijdslot(object):

	def __init__(self, naam, les):
		self.naam = naam # uniek id
		self.les = les # les dat op dit tijdstip plaats vindt 

######################################################################

class student(object):

	def __init__(self, studentnummer, inschrijvingen):
		self.studentnummer = studentnummer # uniek id
		self.inschrijvingen = inschrijvingen # lijst met Vak objecten