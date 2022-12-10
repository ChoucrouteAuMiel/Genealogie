import config
from SQL.ImportIndividual import *
from SQL.BddRelay import *
from SQL.InitBaseStep import *

class Individual:
    def __init__(self, lastName, firstName) -> None:
        self.lastName = lastName
        self.firstName = firstName
        self.id = "111"
        self.birthDate ="11-11-2011"
        self.birthPlace = "LE HAVRE"
        self.deathDate = "11-11-2012"
        self.deathPlace = "Ici"
        self.sex = "H"
        self.job = "Analyste développeur"

bddRelay = Relay(config.bddUrl,config.id,config.pwd)

if not config.bddIsInitialised :
    initBaseStep(bddRelay)

iCreator = IndividualCreator(bddRelay)
iCreator.addIndividual(Individual("du Portal", "FOULIX"))
bddRelay.close()